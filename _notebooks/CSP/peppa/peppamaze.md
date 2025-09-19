---
layout: default
title: Peppa Pig Maze
description: Guide Peppa Pig through a hay maze to learn CS fun facts
background: images/peppapigducks.jpg  
permalink: /peppa-maze/
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peppa Pig Hay Maze</title>
    <style>
        body { 
            margin: 0; 
            font-family: 'Comic Sans MS', cursive, sans-serif; 
            text-align: center; 
            background: #87CEEB; 
            background-image: linear-gradient(to bottom, #87CEEB, #64b5f6);
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }
        #mazeCanvas { 
            border: 4px solid #8B4513; 
            display: block; 
            margin: 20px auto; 
            background: #f0f0f0; 
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            border-radius: 8px;
        }
        #factBox, #linksBox {
            margin: 10px auto; 
            padding: 15px; 
            width: 80%;
            max-width: 600px;
            background: rgba(255,253,208,0.95); 
            border-radius: 15px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.3);
            border: 2px solid #8B4513;
            color: #5D4037;
        }
        h1 {
            color: #8B4513;
            text-shadow: 2px 2px 0px #FFC107;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        h3 {
            color: #5D4037;
            margin-top: 0;
        }
        ul {
            text-align: left;
            display: inline-block;
            margin: 0;
            padding: 0;
            list-style-type: none;
        }
        li {
            margin-bottom: 8px;
        }
        a {
            color: #8B4513;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        a:hover {
            color: #FF5722;
            text-decoration: underline;
        }
        .instructions {
            background: rgba(255, 255, 255, 0.9);
            padding: 10px;
            border-radius: 10px;
            margin: 10px auto;
            max-width: 600px;
            border: 2px dashed #8B4513;
        }
    </style>
</head>
<body>
    <h1>Peppa Pig's Hay Maze Adventure</h1>
    
    <div class="instructions">
        <p>🐷 Press number keys 1–9 to guide Peppa through the hay maze!</p>
    </div>
    
    <canvas id="mazeCanvas"></canvas>
    
    <div id="factBox">Find all the numbers to learn CS facts!</div>
    
    <div id="linksBox" style="display:none;">
        <h3>🎓 Explore Computer Science:</h3>
        <ul>
            <li><a href="#" target="_blank">LxD Setup on Mac</a></li>
            <li><a href="#" target="_blank">LxD Setup for Make</a></li>
            <li><a href="#" target="_blank">LxD Setup on Windows</a></li>
            <li><a href="#" target="_blank">LxD Setup for venv</a></li>
        </ul>
    </div>

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

            let peppa = {x:0, y:0};

            // Function to draw hay bale
            function drawHayBale(x, y) {
                // Hay bale base
                ctx.fillStyle = "#D2B55B";
                ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
                
                // Hay texture lines
                ctx.strokeStyle = "#A68A56";
                ctx.lineWidth = 2;
                
                // Horizontal lines
                for (let i = 1; i < 4; i++) {
                    ctx.beginPath();
                    ctx.moveTo(x * cellSize, y * cellSize + i * (cellSize/4));
                    ctx.lineTo((x+1) * cellSize, y * cellSize + i * (cellSize/4));
                    ctx.stroke();
                }
                
                // Vertical lines
                for (let i = 1; i < 4; i++) {
                    ctx.beginPath();
                    ctx.moveTo(x * cellSize + i * (cellSize/4), y * cellSize);
                    ctx.lineTo(x * cellSize + i * (cellSize/4), (y+1) * cellSize);
                    ctx.stroke();
                }
                
                // Darker border
                ctx.strokeStyle = "#8B4513";
                ctx.lineWidth = 3;
                ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);
            }

            function drawBackground() {
                // Draw sky
                ctx.fillStyle = "#87CEEB";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Draw simple ground
                ctx.fillStyle = "#8BC34A";
                ctx.fillRect(0, canvas.height * 0.7, canvas.width, canvas.height * 0.3);
                
                // Draw clouds
                ctx.fillStyle = "white";
                ctx.beginPath();
                ctx.arc(100, 80, 30, 0, Math.PI * 2);
                ctx.arc(130, 70, 35, 0, Math.PI * 2);
                ctx.arc(160, 80, 30, 0, Math.PI * 2);
                ctx.fill();
                
                ctx.beginPath();
                ctx.arc(400, 120, 25, 0, Math.PI * 2);
                ctx.arc(430, 110, 30, 0, Math.PI * 2);
                ctx.arc(460, 120, 25, 0, Math.PI * 2);
                ctx.fill();
            }

            function drawMaze(){
                // Draw semi-transparent maze cells over the background
                for(let y = 0; y < rows; y++){
                    for(let x = 0; x < cols; x++){
                        if (maze[y][x] === 1) {
                            drawHayBale(x, y);
                        } else {
                            ctx.fillStyle = "rgba(255, 255, 255, 0.3)";
                            ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
                        }
                    }
                }
            
                // Draw numbers
                ctx.fillStyle = "#8B4513";
                ctx.font = "bold 24px Arial";
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                for(const num in numbers){
                    const pos = numbers[num];
                    ctx.fillText(num, pos.x * cellSize + cellSize / 2, pos.y * cellSize + cellSize / 2);
                }
            }

            function drawPeppa(){
                // Draw Peppa as a pink circle with a simple face
                ctx.fillStyle = "#FFB6C1";
                ctx.beginPath();
                ctx.arc(peppa.x * cellSize + cellSize/2, peppa.y * cellSize + cellSize/2, cellSize/2, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw simple face
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.arc(peppa.x * cellSize + cellSize/2 - 10, peppa.y * cellSize + cellSize/2 - 5, 5, 0, Math.PI * 2);
                ctx.arc(peppa.x * cellSize + cellSize/2 + 10, peppa.y * cellSize + cellSize/2 - 5, 5, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw smile
                ctx.beginPath();
                ctx.arc(peppa.x * cellSize + cellSize/2, peppa.y * cellSize + cellSize/2 + 5, 10, 0, Math.PI);
                ctx.stroke();
                
                // Draw pig snout
                ctx.fillStyle = "#FF9AAF";
                ctx.beginPath();
                ctx.arc(peppa.x * cellSize + cellSize/2, peppa.y * cellSize + cellSize/2, 12, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw nostrils
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.arc(peppa.x * cellSize + cellSize/2 - 5, peppa.y * cellSize + cellSize/2, 3, 0, Math.PI * 2);
                ctx.arc(peppa.x * cellSize + cellSize/2 + 5, peppa.y * cellSize + cellSize/2, 3, 0, Math.PI * 2);
                ctx.fill();
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

            // Start the animation
            update();

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
</body>
</html>