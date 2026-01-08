// MorningPal - Options Script

document.addEventListener('DOMContentLoaded', loadSettings);
document.getElementById('saveBtn').addEventListener('click', saveSettings);
document.getElementById('logoutBtn').addEventListener('click', logout);

async function loadSettings() {
  const settings = await chrome.storage.local.get([
    'reminderTime',
    'weekendReminder', 
    'reminderEnabled',
    'token',
    'userEmail'
  ]);
  
  document.getElementById('reminderTime').value = settings.reminderTime || '09:00';
  document.getElementById('weekendReminder').checked = settings.weekendReminder || false;
  document.getElementById('reminderEnabled').checked = settings.reminderEnabled !== false;
  
  if (settings.token) {
    document.getElementById('userEmail').textContent = settings.userEmail || '已登录';
    document.getElementById('userStatus').textContent = '已登录';
  }
}

async function saveSettings() {
  const settings = {
    reminderTime: document.getElementById('reminderTime').value,
    weekendReminder: document.getElementById('weekendReminder').checked,
    reminderEnabled: document.getElementById('reminderEnabled').checked
  };
  
  await chrome.storage.local.set(settings);
  
  const status = document.getElementById('saveStatus');
  status.textContent = '✅ 设置已保存';
  setTimeout(() => { status.textContent = ''; }, 2000);
}

async function logout() {
  await chrome.storage.local.remove(['token', 'userEmail', 'streak']);
  document.getElementById('userEmail').textContent = '未登录';
  document.getElementById('userStatus').textContent = '请在弹窗中登录';
}
