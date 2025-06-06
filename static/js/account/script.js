document.addEventListener("DOMContentLoaded", function () {
  const calendarEl = document.getElementById("calendar");
  if (!calendarEl) return;

  const activityData = JSON.parse(calendarEl.dataset.activity);
  const calendar = calendarEl;
  const monthLabels = document.getElementById("month-labels");

  const weeks = [];
  let week = [];

  activityData.forEach((entry) => {
    const date = new Date(entry.date);
    if (date.getDay() === 0 && week.length) {
      weeks.push(week);
      week = [];
    }
    week.push(entry);
  });
  if (week.length) weeks.push(week);

  let lastMonth = '';
  weeks.forEach((week) => {
    const col = document.createElement('div');
    col.className = 'week';

    week.forEach((day) => {
      const box = document.createElement('div');
      box.className = 'day';
      box.setAttribute('data-count', Math.min(day.count, 4));
      box.title = `${day.date}: ${day.count} activity`;
      col.appendChild(box);
    });

    const firstDate = new Date(week[0].date);
    const month = firstDate.toLocaleString('default', { month: 'short' });

    const label = document.createElement('div');
    label.style.width = '12px';

    if (month !== lastMonth) {
      label.textContent = month;
      lastMonth = month;
    }

    monthLabels.appendChild(label);
    calendar.appendChild(col);
  });
});
