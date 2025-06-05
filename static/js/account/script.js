document.addEventListener("DOMContentLoaded", function () {
  const data = JSON.parse(document.getElementById("calendar").dataset.activity);
  const calendar = document.getElementById("calendar");

  const getColor = (count) => {
    if (count === 0) return "#ebedf0";
    if (count <= 2) return "#c6e48b";
    if (count <= 5) return "#7bc96f";
    return "#239a3b";
  };

  data.forEach((day) => {
    const cell = document.createElement("div");
    cell.style.backgroundColor = getColor(day.count);
    cell.title = `${day.date}: ${day.count} activities`;
    calendar.appendChild(cell);
  });

  // Streak calculation
  let currentStreak = 0,
    maxStreak = 0,
    tempStreak = 0;

  for (let i = data.length - 1; i >= 0; i--) {
    if (data[i].count > 0) currentStreak++;
    else break;
  }

  data.forEach((day) => {
    if (day.count > 0) tempStreak++;
    else tempStreak = 0;
    maxStreak = Math.max(maxStreak, tempStreak);
  });

  document.getElementById("current-streak").innerText = `${currentStreak} Days`;
  document.getElementById("max-streak").innerText = `${maxStreak} Days`;
});
