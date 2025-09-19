---
layout: default
title: Peppa Pig Maze
description: Guide Peppa Pig through a maze to learn CS fun facts
background: images/blankpeppa.png   
permalink: /peppa-maze/
---

<canvas id="mazeCanvas"></canvas>
<div id="factBox">🐷 Press keys 1–9 to send Peppa to numbers in the maze!</div>
<div id="linksBox" style="display:none;">
  <h3>🎓 Explore Computer Science:</h3>
  <ul>
    <li><a href="{{ '/lxd/setup/mac' | relative_url }}" target="_blank">LxD Setup on Mac</a></li>
    <li><a href="{{ '/lxd/setup/make' | relative_url }}" target="_blank">LxD Setup for Make</a></li>
    <li><a href="{{ '/lxd/setup/windows' | relative_url }}" target="_blank">LxD Setup on Windows</a></li>
    <li><a href="{{ '/lxd/setup/venv' | relative_url }}" target="_blank">LxD Setup for venv</a></li>
  </ul>
</div>

<style>
  body { margin: 0; font-family: Arial, sans-serif; text-align: center; }
  #mazeCanvas { border: 2px solid black; display: block; margin: 20px auto; background: #f0f0f0; }
  #factBox, #linksBox {
    margin: 10px auto; padding: 10px; width: 80%;
    background: rgba(255,255,255,0.9); border-radius: 10px;
    box-shadow: 0 3px 6px rgba(0,0,0,0.3);
  }
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("mazeCanvas");
  const ctx = canvas.getContext("2d");
  canvas.width = 600;
  canvas.height = 600;

  const cellSize = 60, rows = 10, cols = 10;
  const maze = [
    [0,0,1,0,0,0,0,1,0,0],
    [1,0,1,0,1,1,0,1,0,1],
    [0,0,0,0,0,1,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,0,1,0,0],
    [0,1,0,1,1,1,0,1,0,1],
    [0,1,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0],
  ];

  const numbers = {
    "1": {x:1,y:0}, "2": {x:4,y:0}, "3": {x:8,y:0},
    "4": {x:0,y:4}, "5": {x:5,y:4}, "6": {x:9,y:4},
    "7": {x:0,y:8}, "8": {x:5,y:8}, "9": {x:9,y:9}
  };

  const facts = {
    "1":"💻 Run `make clean` then `make` to fix builds.",
    "2":"🐍 Activate venv: Windows → `venv\\\\Scripts\\\\activate`, Mac/Linux → `source venv/bin/activate`.",
    "3":"🌐 Install Ubuntu: `wsl --install` or bootable USB.",
    "4":"🔧 Install VS Code and extensions.",
    "5":"🤖 Clone repos with `git clone ...`.",
    "6":"💾 Permalink: add `permalink: /page/` in front matter.",
    "7":"📤 Push to GitHub: `git add .`, `git commit -m`, `git push origin main`.",
    "8":"🎨 Change theme in VS Code: `Ctrl+K Ctrl+T`.",
    "9":"🎉 Finished the maze! Explore links below."
  };


// Background image
const bgImg = new Image();
bgImg.src = "/images/blankpeppa.png";  // <-- your uploaded file path

// Draw background
function drawBackground() {
  ctx.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
}

// Draw maze (transparent paths, solid walls)
function drawMaze() {
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      if (maze[y][x] === 1) {
        ctx.fillStyle = "#444"; // walls
        ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
      }
      ctx.strokeStyle = "#000"; // grid
      ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);
    }
  }
  // Draw numbers
  ctx.fillStyle = "blue";
  ctx.font = "20px Arial";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  for (const num in numbers) {
    const pos = numbers[num];
    ctx.fillText(
      num,
      pos.x * cellSize + cellSize / 2,
      pos.y * cellSize + cellSize / 2
    );
  }
}

// Draw Peppa (pink circle for now)
function drawPeppa() {
  ctx.beginPath();
  ctx.arc(
    peppa.x * cellSize + cellSize / 2,
    peppa.y * cellSize + cellSize / 2,
    cellSize / 3,
    0,
    Math.PI * 2
  );
  ctx.fillStyle = "pink";
  ctx.fill();
  ctx.closePath();
}

// Show fun facts
function showFact(num) {
  const factBox = document.getElementById("factBox");
  factBox.textContent = funFacts[num] || "🐷 Oink! No fact here.";
}

// Handle keypress
document.addEventListener("keydown", (e) => {
  if (e.key >= "1" && e.key <= "9") {
    const pos = numbers[e.key];
    if (pos) {
      peppa.x = pos.x;
      peppa.y = pos.y;
      showFact(e.key);
      if (e.key === "9") {
        document.getElementById("linksBox").style.display = "block";
      }
    }
  }
});

// Game loop
function update(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  if (bgImg.complete) {
    drawBackground();
  }
  drawMaze();
  drawPeppa();
  requestAnimationFrame(update);
}

bgImg.onload = () => update();
</script>