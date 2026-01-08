// MorningPal - Popup Script

const API_BASE = 'http://localhost:8000/api';

// DOM Elements
const loginView = document.getElementById('loginView');
const registerView = document.getElementById('registerView');
const chatView = document.getElementById('chatView');
const loading = document.getElementById('loading');
const messages = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const streak = document.getElementById('streak');

// State
let token = null;
let conversationId = null;

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  const stored = await chrome.storage.local.get(['token', 'streak']);
  if (stored.token) {
    token = stored.token;
    showChat();
    loadGreeting();
  }
  if (stored.streak) {
    streak.textContent = `🔥 ${stored.streak}天`;
  }
});

// Event Listeners
document.getElementById('loginBtn').addEventListener('click', login);
document.getElementById('registerBtn').addEventListener('click', register);
document.getElementById('showRegisterBtn').addEventListener('click', () => {
  loginView.classList.add('hidden');
  registerView.classList.remove('hidden');
});
document.getElementById('showLoginBtn').addEventListener('click', () => {
  registerView.classList.add('hidden');
  loginView.classList.remove('hidden');
});
document.getElementById('sendBtn').addEventListener('click', sendMessage);
document.getElementById('settingsBtn').addEventListener('click', () => {
  chrome.runtime.openOptionsPage();
});
messageInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage();
});

// Functions
async function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const errorEl = document.getElementById('loginError');
  
  if (!email || !password) {
    errorEl.textContent = '请填写邮箱和密码';
    return;
  }
  
  showLoading();
  try {
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);
    
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      body: formData
    });
    
    if (!res.ok) throw new Error('登录失败');
    
    const data = await res.json();
    token = data.access_token;
    await chrome.storage.local.set({ token });
    showChat();
    loadGreeting();
  } catch (e) {
    errorEl.textContent = '登录失败，请检查邮箱和密码';
  }
  hideLoading();
}

async function register() {
  const email = document.getElementById('regEmail').value;
  const password = document.getElementById('regPassword').value;
  const errorEl = document.getElementById('registerError');
  
  if (!email || !password) {
    errorEl.textContent = '请填写邮箱和密码';
    return;
  }
  
  showLoading();
  try {
    const res = await fetch(`${API_BASE}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    
    if (!res.ok) throw new Error('注册失败');
    
    const data = await res.json();
    token = data.access_token;
    await chrome.storage.local.set({ token });
    showChat();
    loadGreeting();
  } catch (e) {
    errorEl.textContent = '注册失败，邮箱可能已被使用';
  }
  hideLoading();
}

async function loadGreeting() {
  showLoading();
  try {
    const res = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ message: '开始新的一天的对话，请主动问候我' })
    });
    
    if (!res.ok) throw new Error('Failed');
    
    const data = await res.json();
    conversationId = data.conversation_id;
    addMessage('assistant', data.message);
  } catch (e) {
    addMessage('assistant', '早上好！今天感觉怎么样？😊');
  }
  hideLoading();
}

async function sendMessage() {
  const text = messageInput.value.trim();
  if (!text) return;
  
  messageInput.value = '';
  addMessage('user', text);
  showLoading();
  
  try {
    const res = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ 
        message: text,
        conversation_id: conversationId
      })
    });
    
    if (!res.ok) throw new Error('Failed');
    
    const data = await res.json();
    conversationId = data.conversation_id;
    addMessage('assistant', data.message);
    
    // Update streak
    const stored = await chrome.storage.local.get(['streak']);
    const newStreak = (stored.streak || 0) + 1;
    await chrome.storage.local.set({ streak: newStreak });
    streak.textContent = `🔥 ${newStreak}天`;
  } catch (e) {
    addMessage('assistant', '抱歉，出了点问题。请稍后再试。');
  }
  hideLoading();
}

function addMessage(role, content) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.textContent = content;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function showChat() {
  loginView.classList.add('hidden');
  registerView.classList.add('hidden');
  chatView.classList.remove('hidden');
}

function showLoading() {
  loading.classList.remove('hidden');
}

function hideLoading() {
  loading.classList.add('hidden');
}
