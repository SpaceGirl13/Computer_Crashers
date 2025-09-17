---
layout: base
title: Peppa Pig Maze
description: Guide Peppa Pig through a maze to learn CS fun facts
sprite: images/peppapig.png
permalink: /peppa-maze
---

<canvas id="mazeCanvas"></canvas>
<div id="factBox">🐷 Use keys 1–9 to send Peppa to numbers in the maze!</div>
<div id="linksBox" style="display:none;">
  <h3>🎓 Explore Computer Science:</h3>
  <ul>
    <li><a href="https://spacegirl13.github.io/Computer_Crashers/lxd/setup/mac" target="_blank">LxD Setup on Mac</a></li>
    <li><a href="https://spacegirl13.github.io/Computer_Crashers/lxd/setup/make" target="_blank">LxD Setup for Make</a></li>
    <li><a href="https://spacegirl13.github.io/Computer_Crashers/lxd/setup/windows" target="_blank">LxD Setup on Windows</a></li>
    <li><a href="https://spacegirl13.github.io/Computer_Crashers/lxd/setup/venv" target="_blank">LxD Setup for venv</a></li>
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

{% raw %}
<script>
document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("mazeCanvas");
  const ctx = canvas.getContext("2d");
  canvas.width = 600;
  canvas.height = 600;

  const cellSize = 60; // 10x10 grid
  const rows = 10, cols = 10;

  // Simple maze layout (0 = path, 1 = wall)
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
    "1": {x: 1, y: 0},
    "2": {x: 4, y: 0},
    "3": {x: 8, y: 0},
    "4": {x: 0, y: 4},
    "5": {x: 5, y: 4},
    "6": {x: 9, y: 4},
    "7": {x: 0, y: 8},
    "8": {x: 5, y: 8},
    "9": {x: 9, y: 9}, // maze exit
  };

  const facts = {
    "1": "💻 Fixing make commands: If make fails, often it’s because the Makefile has a typo or a missing dependency. Run make clean first, then try again.",
    "2": "🖥️ Using venv: run ./scripts/venv.sh, then source venv/bin/activate",
    "3": "🌐 Installing ubuntu: You can install Ubuntu alongside Windows using WSL (Windows Subsystem for Linux) or by creating a bootable USB and installing it directly.",
    "4": "🔐 Installing VScode: Go to code.visualstudio.com, download the installer, and add the recommended extensions for Python, Git, and Markdown.",
    "5": "🤖 Cloning a directory: To clone a repository from GitHub, copy its HTTPS link and run these commands in your terminal: git clone https://github.com/username/repo.git and cd repo.",
    "6": "💾 Making a permalink: At the top of your .md file, add YAML front matter and add permalink: with something like /maze/.",
    "7": "📱 Pushing to Github: Save all changes made in your code, stage all changes, name your change, press 'Commit & Push'.",
    "8": "⚡ Changing the theme in VScode: type make whatever theme you what (i.e. minima, cayman) in your local host terminal.",
    "9": "🎉 You completed the maze! To add directories or files to your own repository: Drag and drop the directory or file into your own."
  };

  const factBox = document.getElementById("factBox");
  const linksBox = document.getElementById("linksBox");

  // Load Peppa sprite
  const peppaImg = new Image();
  peppaImg.src = "{{page.sprite}}";

  let peppa = {x:0, y:0}; // grid coords
  let target = null;

  function drawMaze() {
    for (let y=0; y<rows; y++) {
      for (let x=0; x<cols; x++) {
        ctx.fillStyle = maze[y][x] === 1 ? "#333" : "#fff";
        ctx.fillRect(x*cellSize, y*cellSize, cellSize, cellSize);
        ctx.strokeRect(x*cellSize, y*cellSize, cellSize, cellSize);
      }
    }
    // Draw numbers
    ctx.fillStyle = "blue";
    ctx.font = "20px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    for (const num in numbers) {
      const pos = numbers[num];
      ctx.fillText(num, pos.x*cellSize + cellSize/2, pos.y*cellSize + cellSize/2);
    }
  }

  function drawPeppa() {
    ctx.drawImage(peppaImg, peppa.x*cellSize, peppa.y*cellSize, cellSize, cellSize);
  }

  function update() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    drawMaze();
    drawPeppa();
    requestAnimationFrame(update);
  }

  peppaImg.onload = () => {
    update();
  };

  function movePeppaTowardTarget() {
    if (!target) return;
    if (peppa.x < target.x) peppa.x++;
    else if (peppa.x > target.x) peppa.x--;
    else if (peppa.y < target.y) peppa.y++;
    else if (peppa.y > target.y) peppa.y--;

    if (peppa.x === target.x && peppa.y === target.y) {
      const num = Object.keys(numbers).find(k => numbers[k].x === target.x && numbers[k].y === target.y);
      if (num) {
        factBox.textContent = facts[num];
        if (num === "9") {
          linksBox.style.display = "block";
        }
      }
      target = null;
    } else {
      setTimeout(movePeppaTowardTarget, 300);
    }
  }

  document.addEventListener("keydown", (e) => {
    if (numbers[e.key]) {
      target = numbers[e.key];
      movePeppaTowardTarget();
    }
  });
});
</script>
{% endraw %}
