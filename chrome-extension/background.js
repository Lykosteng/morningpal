// MorningPal - Background Service Worker

const ALARM_NAME = 'morningpal-reminder';

// 初始化
chrome.runtime.onInstalled.addListener(async () => {
  console.log('MorningPal installed');
  await setupAlarm();
});

// 监听 alarm
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === ALARM_NAME) {
    showNotification();
  }
});

// 监听通知点击
chrome.notifications.onClicked.addListener(() => {
  chrome.action.openPopup();
});

// 设置定时提醒
async function setupAlarm() {
  const settings = await chrome.storage.local.get(['reminderTime', 'reminderEnabled', 'weekendReminder']);
  
  if (settings.reminderEnabled === false) {
    chrome.alarms.clear(ALARM_NAME);
    return;
  }
  
  const time = settings.reminderTime || '09:00';
  const [hours, minutes] = time.split(':').map(Number);
  
  const now = new Date();
  const scheduled = new Date();
  scheduled.setHours(hours, minutes, 0, 0);
  
  if (scheduled <= now) {
    scheduled.setDate(scheduled.getDate() + 1);
  }
  
  chrome.alarms.create(ALARM_NAME, {
    when: scheduled.getTime(),
    periodInMinutes: 24 * 60
  });
  
  console.log('Alarm set for:', scheduled);
}

// 显示通知
function showNotification() {
  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'icons/icon-128.png',
    title: 'MorningPal - 小航',
    message: '早上好！准备好开始新的一天了吗？点击和我聊聊 ⛵',
    priority: 2
  });
}

// 监听设置变化
chrome.storage.onChanged.addListener((changes, area) => {
  if (area === 'local' && (changes.reminderTime || changes.reminderEnabled)) {
    setupAlarm();
  }
});
