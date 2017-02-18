<h1 align="center">돌려방</h1>

<p align="center"><a href="hskang9.pythonanywhere.com
" target="_blank"><img width="480" alt="돌려방" src="https://s6.postimg.org/47g5ir0e9/webvr.png"></a></p>

<p align="center"><b>방을 돌려보고 둘러보는 가상현실(VR) 주택 임대 서비스 모바일 웹 앱</b></p>

<p align="center">
  <a href="">
    <img src="http://img.shields.io/pypi/v/nine.svg" alt="Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/npm/l/aframe.svg?style=flat-square" alt="License">
  </a>
</p>

## Usage

### Basic Example

To get started playing now, open this [**CodePen example
scene**](http://codepen.io/sudosudoohio/pen/GrxOzY).

```html
<html>

<head>
  <script src="https://aframe.io/releases/0.4.0/aframe.min.js"></script>
  <script>
               unction initElement() {
                 var navVR = document.getElementById("navigate");
                 navVR.onclick = navigate;
               ;
               function navigate() {
                 window.location.href = "http://www.naver.com";
               
  </script>
</head>

<body onload="initElement();">
  <main>
    <div>
      <a-scene inspector="url: https://aframe.io/releases/0.3.0/aframe-inspector.min.js">
        <a-assets>
          <img id="sphereTexture" color="#fff">
          <img id="skyTexture" src="https://raw.githubusercontent.com/hskang9/WebVR/master/web/static/photos/hacking-room1.jpg" rotation="0 -130 0">
        </a-assets>
        <a-sphere id="navigate" color="#FFF" width="2" height="2" depth="2" position="20 2 -10" rotation="0 0 45" scale="2 2 2" src="#sphereTexture">
          <a-animation attribute="position" to="20 2.2 -10" direction="alternate" dur="2000" repeat="indefinite"></a-animation>
          <!-- 커서가 오브젝트를 가리킬 때 애니메이션-->
          <a-animation attribute="scale" begin="mouseenter" dur="300" to="2.3 2.3 2.3"></a-animation>
          <a-animation attribute="scale" begin="mouseleave" dur="300" to="2 2 2"></a-animation>
        </a-sphere>
        <a-sky src="#skyTexture"></a-sky>
        <div class="a-exit-vr" aframe-injected="" style="display: block;"><button class="a-enter-vr-button" aframe-injected=""></button></div>
        <a-camera>
          <a-cursor></a-cursor>
        </a-camera>
      </a-scene>
    </div>
  </main>

  <body>

</html>
```

## Local Development

```sh
git clone https://github.com/hskang9/WebVR.git  # Clone the repository.
cd WebVR && python manage.py runserver  # Start the local development server.
```

And open in your browser **[http://localhost:8000](http://localhost:8000)** or **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

### Generating Builds


## Questions

For questions and support, [post an issue on this repository](https://github.com/hskang9/WebVR/issues).


## License

This program is free software and is distributed under an [MIT License](LICENSE).
