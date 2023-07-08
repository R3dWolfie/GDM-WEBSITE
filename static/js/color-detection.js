// static/js/color-detection.js
document.addEventListener('DOMContentLoaded', function() {
  var video = document.querySelector('.fullscreen-video');
  var textColorElements = document.querySelectorAll('.cover-heading, .lead, .card-title, .card-text, .btn-primary, footer p');

  video.addEventListener('play', function() {
    var canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    var imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    var data = imageData.data;
    var r = 0;
    var g = 0;
    var b = 0;

    for (var i = 0; i < data.length; i += 4) {
      r += data[i];
      g += data[i + 1];
      b += data[i + 2];
    }

    var pixelCount = data.length / 4;
    var avgR = Math.floor(r / pixelCount);
    var avgG = Math.floor(g / pixelCount);
    var avgB = Math.floor(b / pixelCount);

    var brightness = (avgR * 299 + avgG * 587 + avgB * 114) / 1000;

    if (brightness > 125) {
      // Light background, set text color to black
      for (var j = 0; j < textColorElements.length; j++) {
        textColorElements[j].style.color = '#000000';
      }
    } else {
      // Dark background, set text color to white
      for (var k = 0; k < textColorElements.length; k++) {
        textColorElements[k].style.color = '#ffffff';
      }
    }
  });
});
