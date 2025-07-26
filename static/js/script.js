
/* script.js */
particlesJS("particles-js", {
  "particles": {
    "number": {
      "value": 120
    },
    "color": {
      "value": "#ffffff"
    },
    "shape": {
      "type": "circle"
    },
    "opacity": {
      "value": 0.5
    },
    "size": {
      "value": 1.5
    },
    "move": {
      "enable": true,
      "speed": 0.3
    }
  },
  "interactivity": {
    "events": {
      "onhover": {
        "enable": true,
        "mode": "repulse"
      }
    }
  },
  "retina_detect": true
});
function updateFileName() {
  const input = document.getElementById('fileInput');
  const label = document.getElementById('fileLabel');
  if (input.files.length > 0) {
    label.textContent = `📄 ${input.files[0].name}`;
  } else {
    label.textContent = "🚀 Click here to choose a file";
  }
}

