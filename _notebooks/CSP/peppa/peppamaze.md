---
layout: default
title: Peppa Pig Maze
description: Guide Peppa Pig through a maze to learn CS fun facts
background: images/peppapigducks.jpg   
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
  body { margin: 0; font-family: Arial, sans-serif; text-align: center; background: #87CEEB; }
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

  const factBox = document.getElementById("factBox");
  const linksBox = document.getElementById("linksBox");

  // Create separate images for background and Peppa
  const bgImg = new Image();
  const peppaImg = new Image();
  
  // Set image sources - make sure these paths are correct
  bgImg.src = "{{ 'images/peppapigducks.jpg' | relative_url }}";
  peppaImg.src = "{{ 'images/peppapigducks.jpg' | relative_url }}"; // This should be a different image for Peppa

  let peppa = {x:0, y:0};

  function drawBackground() {
    if (bgImg.complete) {
      // Draw the background image to cover the entire canvas
      ctx.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
    } else {
      // Fallback if image doesn't load
      ctx.fillStyle = "#87CEEB"; // Sky blue
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
  }

  function drawMaze(){
    // Draw semi-transparent maze cells over the background
    for(let y = 0; y < rows; y++){
      for(let x = 0; x < cols; x++){
        ctx.fillStyle = maze[y][x] === 1 ? "rgba(68, 68, 68, 0.7)" : "rgba(255, 255, 255, 0.7)";
        ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
        ctx.strokeStyle = "#000"; 
        ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);
      }
    }
    
    // Draw numbers
    ctx.fillStyle = "blue"; 
    ctx.font = "20px Arial";
    ctx.textAlign = "center"; 
    ctx.textBaseline = "middle";
    for(const num in numbers){
      const pos = numbers[num];
      ctx.fillText(num, pos.x * cellSize + cellSize / 2, pos.y * cellSize + cellSize / 2);
    }
  }

  function drawPeppa(){ 
    if (peppaImg.complete) {
      ctx.drawImage(peppaImg, peppa.x * cellSize, peppa.y * cellSize, cellSize, cellSize);
    } else {
      // Fallback if Peppa image doesn't load
      ctx.fillStyle = "pink";
      ctx.beginPath();
      ctx.arc(peppa.x * cellSize + cellSize/2, peppa.y * cellSize + cellSize/2, cellSize/2, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function update(){
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw background
    drawBackground();
    
    // Draw maze on top
    drawMaze();
    
    // Draw Peppa on top of everything
    drawPeppa();
    
    requestAnimationFrame(update);
  }

  // Start the animation once images are loaded
  let imagesLoaded = 0;
  const totalImages = 2;
  
  function checkAllImagesLoaded() {
    imagesLoaded++;
    if (imagesLoaded === totalImages) {
      update();
    }
  }
  
  bgImg.onload = checkAllImagesLoaded;
  bgImg.onerror = function() {
    console.error("Background image failed to load");
    checkAllImagesLoaded();
  };
  
  peppaImg.onload = checkAllImagesLoaded;
  peppaImg.onerror = function() {
    console.error("Peppa image failed to load");
    checkAllImagesLoaded();
  };

  // If images are already loaded (cached), trigger load manually
  if (bgImg.complete && peppaImg.complete) {
    update();
  }

  function findPath(start, end){
    const q = [[start]], vis = new Set([`${start.x},${start.y}`]);
    while(q.length){
      const path = q.shift(); 
      const {x, y} = path[path.length-1];
      if(x === end.x && y === end.y) return path;
      for(const m of [{x:x+1,y}, {x:x-1,y}, {x, y:y+1}, {x, y:y-1}]){
        if(m.x >= 0 && m.x < cols && m.y >= 0 && m.y < rows && 
           maze[m.y][m.x] === 0 && !vis.has(`${m.x},${m.y}`)){
          vis.add(`${m.x},${m.y}`); 
          q.push([...path, m]);
        }
      }
    } 
    return null;
  }

  function movePeppa(path, num){
    if(!path) return; 
    let step = 0;
    
    function stepMove(){
      if(step < path.length){ 
        peppa = path[step]; 
        step++; 
        setTimeout(stepMove, 300);
      } else { 
        factBox.textContent = facts[num]; 
        if(num === "9") linksBox.style.display = "block"; 
      }
    } 
    stepMove();
  }

  document.addEventListener("keydown", e => {
    if(numbers[e.key]){ 
      const path = findPath(peppa, numbers[e.key]); 
      movePeppa(path, e.key); 
    }
  });
});
</script>