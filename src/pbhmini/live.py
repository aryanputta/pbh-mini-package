"""Generate lightweight browser simulations for the mini package."""

from __future__ import annotations

from pathlib import Path


def write_evaporation_html(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """<!doctype html>
<html><head><meta charset="utf-8"><title>PBH Toy Live Simulation</title>
<style>body{margin:0;background:#101418;color:#edf2f7;font-family:Arial,sans-serif}main{max-width:900px;margin:auto;padding:24px}canvas{width:100%;height:420px;background:#05070a;border:1px solid #39424e}label{display:block;margin:10px 0}</style>
</head><body><main><h1>PBH Evaporation Toy Simulation</h1>
<p>Analytic dM/dt = -alpha/M^2 visualization. Not GRChombo or Einstein Toolkit.</p>
<label>Initial mass log10(g) <input id="mass" type="range" min="7" max="13" step="0.1" value="10"></label>
<label>Remnant mass log10(g) <input id="rem" type="range" min="0" max="9" step="0.1" value="5"></label>
<canvas id="c" width="1100" height="520"></canvas></main><script>
const c=document.getElementById('c'),x=c.getContext('2d'),alpha=Math.pow(5e14,3)/(3*4.35e17);let start=performance.now();
function draw(){const m0=Math.pow(10,+mass.value),r=Math.min(Math.pow(10,+rem.value),.9*m0),p=((performance.now()-start)/25000)%1;
const m=Math.cbrt(Math.max(Math.pow(m0,3)-3*alpha*p*(Math.pow(m0,3)-Math.pow(r,3))/(3*alpha),Math.pow(r,3)));
const rad=20+150*Math.sqrt(m/m0);x.clearRect(0,0,c.width,c.height);x.fillStyle='#05070a';x.fillRect(0,0,c.width,c.height);
let g=x.createRadialGradient(550,230,rad*.6,550,230,rad*2.5);g.addColorStop(0,'#fff');g.addColorStop(.1,'#fbbf24');g.addColorStop(.45,'#dc2626');g.addColorStop(1,'rgba(0,0,0,0)');
x.fillStyle=g;x.beginPath();x.arc(550,230,rad*2.5,0,7);x.fill();x.fillStyle='#000';x.beginPath();x.arc(550,230,rad,0,7);x.fill();
x.fillStyle='#edf2f7';x.font='24px Arial';x.fillText('mass = '+m.toExponential(3)+' g',40,54);x.fillText('relative abundance = '+(m/m0).toExponential(3),40,90);requestAnimationFrame(draw)}draw();
</script></body></html>""",
        encoding="utf-8",
    )
    return path

