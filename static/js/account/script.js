document.addEventListener("DOMContentLoaded", function () {
  const calendarEl = document.getElementById("calendar");
  if (!calendarEl) return;

  const data = JSON.parse(calendarEl.dataset.activity || "[]");

  data.forEach((day) => {
    const cell = document.createElement("div");
    cell.classList.add("calendar-cell");
    cell.style.backgroundColor = getColor(day.count);
    cell.title = `${day.date}: ${day.count} logins`;
    calendarEl.appendChild(cell);
  });

  function getColor(count) {
    if (count === 0) return "#ebedf0"; // light grey
    if (count <= 2) return "#c6e48b";
    if (count <= 5) return "#7bc96f";
    return "#239a3b";
  }
});
