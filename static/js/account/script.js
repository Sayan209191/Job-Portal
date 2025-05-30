document.addEventListener("DOMContentLoaded", () => {
  const calendar = document.getElementById("calendar");

  const DAYS = 30; 
  const activityLevels = Array.from({ length: DAYS }, () => Math.floor(Math.random() * 4));

  // Colors for activity levels matching CSS legends
  const colors = {
    0: "#eaeaea",    // no activity (light gray)
    1: "#c6dbef",    // low
    2: "#6baed6",    // mid
    3: "#2171b5",    // high
  };

  // Create calendar grid container
  calendar.style.display = "grid";
  calendar.style.gridTemplateColumns = "repeat(7, 20px)"; // 7 days per week
  calendar.style.gridGap = "4px";

  // Generate day squares
  for (let i = DAYS - 1; i >= 0; i--) {
    const daySquare = document.createElement("div");
    daySquare.style.width = "20px";
    daySquare.style.height = "20px";
    daySquare.style.borderRadius = "4px";
    daySquare.style.backgroundColor = colors[activityLevels[i]];
    daySquare.title = `Day ${DAYS - i}: Activity level ${activityLevels[i]}`;
    calendar.appendChild(daySquare);
  }
});

