---
layout: opencs
title: Memory Game
permalink: /javascript/project/memory
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Farm Memory Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background: #f0f8ff;
    }
    #timer {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 10px;
      color: darkred;
    }
    .memoryCanvas {
      border: 10px solid #000;
      display: block;
      margin: 0 auto;
      background-size: cover;
      background-position: center;
    }
    /* description styling */
    p.description {
      margin: 12px auto;
      font-size: 16px;
      color: #333;
      max-width: 600px;
      line-height: 1.4;
      text-align: left;
    }
  </style>
</head>
<body>
  <h1>Farm Memory Game</h1>
  <div id="timer">Time Left: 60</div>
  <canvas id="memoryCanvas" class="memoryCanvas" width="600" height="600"></canvas>

  <script>
    const memCanvas = document.getElementById("memoryCanvas");
    const memCtx = memCanvas.getContext("2d");

    const bgImage = new Image();
    bgImage.src = "{{ site.baseurl }}/images/farmbackground.jpg";

    const emojis = ["🦒","🐷","🐰","🐴","🐑","🐶","🐘","🦓"];
    let emojiList = [...emojis, ...emojis];
    emojiList = shuffleArray(emojiList);

    let revealedCells = [];
    let matchedCells = [];

    let timeLeft = 60;
    let timerId = null;

    function shuffleArray(array) {
      let currentIndex = array.length, randomIndex;
      while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
      }
      return array;
    }

    function drawBackground() {
      memCtx.drawImage(bgImage, 0, 0, memCanvas.width, memCanvas.height);
    }

    function drawGrid(cols, rows) {
      const cellWidth = memCanvas.width / cols;
      const cellHeight = memCanvas.height / rows;
      memCtx.strokeStyle = "#000";
      for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
          memCtx.strokeRect(col * cellWidth, row * cellHeight, cellWidth, cellHeight);
        }
      }
    }

    function hideEmojis(cols, rows) {
      drawBackground();
      drawGrid(cols, rows);
      const cellWidth = memCanvas.width / cols;
      const cellHeight = memCanvas.height / rows;

      for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
          if (!matchedCells.some(cell => cell.col === col && cell.row === row)) {
            memCtx.fillStyle = '#CCCCCC';
            memCtx.fillRect(col * cellWidth + 5, row * cellHeight + 5, cellWidth - 10, cellHeight - 10);
          }
        }
      }
    }

    function revealEmojiAt(col, row, emojis) {
      if (matchedCells.some(c => c.col === col && c.row === row)) return;
      if (revealedCells.some(c => c.col === col && c.row === row)) return;

      const cellWidth = memCanvas.width / 4;
      const cellHeight = memCanvas.height / 4;
      const x = col * cellWidth;
      const y = row * cellHeight;
      const emojiIndex = row * 4 + col;
      const emoji = emojis[emojiIndex];

      // Animate flip
      let scale = 1.0;
      let shrinking = true;
      const anim = setInterval(() => {
        drawBackground();
        drawGrid(4, 4);
        hideEmojis(4, 4);

        memCtx.save();
        memCtx.translate(x + cellWidth / 2, y + cellHeight / 2);
        memCtx.scale(scale, 1);

        if (shrinking) {
          memCtx.fillStyle = '#CCCCCC';
          memCtx.fillRect(-cellWidth/2 + 5, -cellHeight/2 + 5, cellWidth - 10, cellHeight - 10);
        } else {
          memCtx.fillStyle = '#FFFFFF';
          memCtx.fillRect(-cellWidth/2 + 5, -cellHeight/2 + 5, cellWidth - 10, cellHeight - 10);
          memCtx.fillStyle = '#000000';
          memCtx.font = "40px Arial";
          memCtx.textAlign = "center";
          memCtx.textBaseline = "middle";
          memCtx.fillText(emoji, 0, 0);
        }

        memCtx.restore();

        if (shrinking) {
          scale -= 0.1;
          if (scale <= 0) shrinking = false;
        } else {
          scale += 0.1;
          if (scale >= 1) {
            clearInterval(anim);
            revealedCells.push({col, row, emoji});
            checkMatch();
          }
        }
      }, 30);
    }

    function checkMatch() {
      if (revealedCells.length === 2) {
        const [first, second] = revealedCells;
        if (first.emoji === second.emoji) {
          matchedCells.push(first, second);
          revealedCells = [];
        } else {
          setTimeout(() => {
            revealedCells = [];
            hideEmojis(4, 4);
          }, 800);
        }
      }
    }

    memCanvas.addEventListener("click", (e) => {
      const rect = memCanvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const col = Math.floor(x / (memCanvas.width / 4));
      const row = Math.floor(y / (memCanvas.height / 4));
      revealEmojiAt(col, row, emojiList);
    });

<<<<<<< HEAD
    // Draw all emojis at the start (for initial reveal)
    drawEmojis(4, 4, emojiList);
</script>

=======
    // Timer
    function startTimer() {
      const timerDisplay = document.getElementById("timer");
      timerId = setInterval(() => {
        timeLeft--;
        timerDisplay.textContent = "Time Left: " + timeLeft;
        if (timeLeft <= 0) {
          clearInterval(timerId);
          alert("⏰ Time's up! Game over.");
        }
        if (matchedCells.length === emojiList.length) {
          clearInterval(timerId);
          alert("🎉 You matched all the animals!");
        }
      }, 1000);
    }

    bgImage.onload = function() {
      drawBackground();
      drawGrid(4, 4);
      setTimeout(() => hideEmojis(4, 4), 2000);
      startTimer();
    };

  </script>

  <!-- fixed paragraphs (note the proper closing tags) -->
  <p class="description"><strong>About this game:</strong></p>
  <p class="description">I customized this memory game by changing the emojis to Peppa Pig themed animals.</p>
  <p class="description">Additionally, I customized this memory game by adding a farm-themed background.</p>
  <p class="description">I also added a flip animation so tiles rotate instead of instantly switching.</p>
  <p class="description">Finally, I included a 60-second countdown timer to add challenge.</p>

</body>
</html>
>>>>>>> 08196ecfe3f500510c0cd2ba131291437e0e10a7
