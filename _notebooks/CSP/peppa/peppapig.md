---
layout: base
title: Peppa Pig Linux
description: Interactive Peppa that follows your cursor and teaches Linux
sprite: images/peppapig.png
permalink: /peppa
---

<div id="peppa-page">
  <div id="peppa-wrapper">
    <!-- Use Jekyll variable for sprite -->
    <img id="peppa" src="{{page.sprite}}" alt="Peppa Pig">
  </div>

  <div id="factBox">🐷 Move your mouse and Peppa will follow! Click anywhere for a Linux fact.</div>
</div>

<style>
  body {
    margin: 0;
    overflow: hidden;
    text-align: center;
    font-family: Arial, sans-serif;
  }
  #peppa-wrapper {
    position: absolute;
    width: 150px;
    pointer-events: none;
    transition: left 0.15s linear, top 0.15s linear;
    transform-origin: center;
  }
  #peppa {
    width: 100%;
    display: block;
    user-select: none;
    -webkit-user-drag: none;
  }
  .walking {
    animation: walkBounce 0.3s infinite alternate;
  }
  @keyframes walkBounce {
    from { transform: translateY(0); }
    to   { transform: translateY(-10px); }
  }
  .flip {
    transform: scaleX(-1);
  }
  #factBox {
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.92);
    padding: 10px 20px;
    border-radius: 12px;
    font-size: 1.05rem;
    max-width: 70%;
    box-shadow: 0 3px 10px rgba(0,0,0,0.18);
  }
</style>

{% raw %}
<script>
document.addEventListener('DOMContentLoaded', function () {
  const wrapper = document.getElementById("peppa-wrapper");
  const peppa = document.getElementById("peppa");
  const factBox = document.getElementById("factBox");

  const facts = [
    "🐧 Linux was created by Linus Torvalds in 1991.",
    "💻 `make` automates builds so you don’t have to compile manually.",
    "📦 Python `venv` keeps each project’s libraries separate.",
    "🌐 Most servers on the internet run Linux.",
    "🔧 Tux the penguin is the Linux mascot.",
    "🚀 Linux is used in spacecraft, Android phones, and supercomputers."
  ];

  let lastX = 0;
  let walkTimeout;

  document.addEventListener("mousemove", (e) => {
    wrapper.style.left = (e.clientX - wrapper.offsetWidth / 2) + "px";
    wrapper.style.top  = (e.clientY - wrapper.offsetHeight / 2) + "px";

    wrapper.classList.add("walking");
    clearTimeout(walkTimeout);
    walkTimeout = setTimeout(() => wrapper.classList.remove("walking"), 300);

    if (e.clientX > lastX) {
      peppa.classList.remove("flip"); // face right
    } else if (e.clientX < lastX) {
      peppa.classList.add("flip"); // face left
    }
    lastX = e.clientX;
  });

  document.addEventListener("click", () => {
    const fact = facts[Math.floor(Math.random() * facts.length)];
    factBox.textContent = fact;
    changeBackground();
  });

  function changeBackground() {
    const r = Math.floor(Math.random() * 200) + 30;
    const g = Math.floor(Math.random() * 200) + 30;
    const b = Math.floor(Math.random() * 200) + 30;
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
  }
});
</script>
{% endraw %}