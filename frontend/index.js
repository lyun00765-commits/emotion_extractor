async function loadConfig() {
    const resp = await fetch("http://localhost:9880/get_config");
    const cfg = await resp.json();
    document.getElementById("api_url").value = cfg.api_url;
    document.getElementById("api_key").value = cfg.api_key;
    document.getElementById("model_select").value = cfg.model;
}

document.getElementById("save_config_btn").onclick = async () => {
    const cfg = {
        api_url: document.getElementById("api_url").value,
        api_key: document.getElementById("api_key").value,
        model: document.getElementById("model_select").value
    };
    await fetch("http://localhost:9880/save_config", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(cfg)
    });
    alert("保存成功");
};

document.getElementById("get_models_btn").onclick = async () => {
    const resp = await fetch("http://localhost:9880/get_models");
    const models = await resp.json();
    const select = document.getElementById("model_select");
    select.innerHTML = "";
    models.forEach(m => {
        const opt = document.createElement("option");
        opt.value = m;
        opt.textContent = m;
        select.appendChild(opt);
    });
};

loadConfig();