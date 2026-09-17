(() => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const scenes = [...document.querySelectorAll("[data-scene]")];
  const progress = document.querySelector(".progress span");
  let queued = false;

  function updateSceneMotion() {
    const viewport = window.innerHeight || 1;
    scenes.forEach((scene) => {
      const rect = scene.getBoundingClientRect();
      const center = rect.top + rect.height / 2;
      const distance = (center - viewport / 2) / viewport;
      scene.style.setProperty("--scene-shift", `${Math.round(distance * -38)}px`);
      scene.style.setProperty("--scene-scale", (1.04 + Math.abs(distance) * 0.04).toFixed(3));
    });
    const height = document.documentElement.scrollHeight - viewport;
    progress.style.setProperty("--progress", `${height > 0 ? (window.scrollY / height) * 100 : 0}%`);
    queued = false;
  }

  function requestUpdate() {
    if (!queued) {
      window.requestAnimationFrame(updateSceneMotion);
      queued = true;
    }
  }

  if (!reducedMotion) {
    window.addEventListener("scroll", requestUpdate, { passive: true });
    window.addEventListener("resize", requestUpdate);
  }
  updateSceneMotion();

  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
      const source = document.getElementById(button.dataset.copyTarget);
      if (!source) return;
      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(source.textContent.trim());
        button.textContent = "Copied";
      } catch {
        button.textContent = "Select text";
      }
      window.setTimeout(() => { button.textContent = original; }, 1800);
    });
  });
})();
