const TEXT = {
  en: {
    title: "Network Inventory", overview: "Overview", devices: "Devices", homeAssistant: "Home Assistant",
    settings: "Settings", integrations: "Integrations", addDevice: "Add device", total: "Total devices", areas: "Areas", brands: "Brands",
    protocols: "Protocols", search: "Search devices…", allProtocols: "All protocols", code: "Device ID",
    name: "Device name", type: "Type", brand: "Brand", model: "Model", area: "Area", address: "MAC / IEEE",
    ip: "IP address", protocol: "Protocol", identifier: "Device identifier", entityName: "Entity name", comments: "Comments", status: "Status",
    actions: "Actions", edit: "Edit", delete: "Delete", save: "Save", cancel: "Cancel", empty: "No devices found.",
    importHa: "Import devices already known to Home Assistant.", import: "Import",
    integration: "Integration", csv: "CSV import", exportCsv: "Export CSV", chooseCsv: "Choose CSV",
    ranges: "Device ID ranges", rangeHelp: "IDs are permanent. A deleted ID is never reused.", start: "Start", end: "End",
    color: "Color", deviceTypes: "Device types (one per line)", brandSettings: "Brands (one per line)", saveSettings: "Save settings", addProtocol: "Add protocol",
    key: "Key", confirmDelete: "Delete this device? Its Device ID will not be reused.", requiredName: "Device name is required.",
    loading: "Loading…", saved: "Saved", imported: "devices imported", skipped: "skipped", error: "Something went wrong",
    autoId: "Assigned automatically when saved", stableId: "The Device ID remains unchanged if the protocol changes.",
    noHa: "All Home Assistant devices have already been imported.", manual: "Manual inventory", unknown: "Unknown",
    allTypes: "All types", allBrands: "All brands", allAreas: "All areas", allStatuses: "All statuses",
    clearFilters: "Clear filters", clearId: "Clear Device ID", newIdHelp: "A new ID will be assigned from the selected protocol when saved.",
    unifi: "UniFi", unifiCloud: "UniFi Cloud", connect: "Connect", disconnect: "Disconnect", refresh: "Refresh",
    apiKey: "API key", selectSite: "Select console / site", connected: "Connected", notConnected: "Not connected",
    unifiHelp: "Connect through the official UniFi Cloud API. The API key is stored privately in Home Assistant.",
    createKey: "Create an API key in UniFi", activeClients: "Connected clients and UniFi infrastructure", added: "Added",
    details: "Details", uplink: "Connected to", connectedSince: "Connected since", firmware: "Firmware",
    noUnifi: "No active UniFi clients or infrastructure were returned.", chooseSiteHelp: "Choose which Dream Machine site to activate.",
    apiKeyPlaceholder: "Paste the UniFi API key", unifiBadge: "View UniFi connection details"
  },
  el: {
    title: "Καταγραφή Συσκευών", overview: "Επισκόπηση", devices: "Συσκευές", homeAssistant: "Home Assistant",
    settings: "Ρυθμίσεις", integrations: "Integrations", addDevice: "Νέα συσκευή", total: "Σύνολο συσκευών", areas: "Χώροι", brands: "Κατασκευαστές",
    protocols: "Πρωτόκολλα", search: "Αναζήτηση συσκευών…", allProtocols: "Όλα τα πρωτόκολλα", code: "Device ID",
    name: "Όνομα συσκευής", type: "Τύπος", brand: "Brand", model: "Μοντέλο", area: "Χώρος", address: "MAC / IEEE",
    ip: "Διεύθυνση IP", protocol: "Πρωτόκολλο", identifier: "Αναγνωριστικό συσκευής", entityName: "Όνομα entity", comments: "Σχόλια", status: "Κατάσταση",
    actions: "Ενέργειες", edit: "Επεξεργασία", delete: "Διαγραφή", save: "Αποθήκευση", cancel: "Ακύρωση", empty: "Δεν βρέθηκαν συσκευές.",
    importHa: "Εισαγωγή συσκευών που γνωρίζει ήδη το Home Assistant.", import: "Εισαγωγή",
    integration: "Integration", csv: "Εισαγωγή CSV", exportCsv: "Εξαγωγή CSV", chooseCsv: "Επιλογή CSV",
    ranges: "Εύρη Device ID", rangeHelp: "Τα ID είναι μόνιμα. Ένα διαγραμμένο ID δεν χρησιμοποιείται ξανά.", start: "Αρχή", end: "Τέλος",
    color: "Χρώμα", deviceTypes: "Τύποι συσκευών (ένας ανά γραμμή)", brandSettings: "Brands (ένα ανά γραμμή)", saveSettings: "Αποθήκευση ρυθμίσεων", addProtocol: "Νέο πρωτόκολλο",
    key: "Κλειδί", confirmDelete: "Να διαγραφεί η συσκευή; Το Device ID της δεν θα χρησιμοποιηθεί ξανά.", requiredName: "Το όνομα είναι υποχρεωτικό.",
    loading: "Φόρτωση…", saved: "Αποθηκεύτηκε", imported: "συσκευές εισήχθησαν", skipped: "παραλείφθηκαν", error: "Παρουσιάστηκε σφάλμα",
    autoId: "Δίνεται αυτόματα κατά την αποθήκευση", stableId: "Το Device ID δεν αλλάζει αν αλλάξει το πρωτόκολλο.",
    noHa: "Όλες οι συσκευές του Home Assistant έχουν ήδη εισαχθεί.", manual: "Χειροκίνητη καταγραφή", unknown: "Άγνωστη",
    allTypes: "Όλοι οι τύποι", allBrands: "Όλα τα brands", allAreas: "Όλοι οι χώροι", allStatuses: "Όλες οι καταστάσεις",
    clearFilters: "Καθαρισμός φίλτρων", clearId: "Διαγραφή Device ID", newIdHelp: "Με την αποθήκευση θα δοθεί νέο ID από το επιλεγμένο πρωτόκολλο.",
    unifi: "UniFi", unifiCloud: "UniFi Cloud", connect: "Σύνδεση", disconnect: "Αποσύνδεση", refresh: "Ανανέωση",
    apiKey: "API key", selectSite: "Επιλογή console / site", connected: "Συνδεδεμένο", notConnected: "Δεν είναι συνδεδεμένο",
    unifiHelp: "Σύνδεση μέσω του επίσημου UniFi Cloud API. Το API key αποθηκεύεται ιδιωτικά στο Home Assistant.",
    createKey: "Δημιουργία API key στο UniFi", activeClients: "Συνδεδεμένοι clients και υποδομή UniFi", added: "Προστέθηκε",
    details: "Πληροφορίες", uplink: "Συνδεδεμένο σε", connectedSince: "Συνδεδεμένο από", firmware: "Firmware",
    noUnifi: "Το UniFi δεν επέστρεψε ενεργούς clients ή συσκευές υποδομής.", chooseSiteHelp: "Επίλεξε ποιο site του Dream Machine θα ενεργοποιηθεί.",
    apiKeyPlaceholder: "Επικόλληση του UniFi API key", unifiBadge: "Πληροφορίες σύνδεσης UniFi"
  }
};

class NetworkInventoryPanel extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.data = null;
    this.view = "overview";
    this.query = "";
    this.protocolFilter = "";
    this.typeFilter = "";
    this.brandFilter = "";
    this.areaFilter = "";
    this.statusFilter = "";
    this._started = false;
  }

  set hass(value) {
    this._hass = value;
    this.lang = value?.language?.startsWith("el") ? "el" : "en";
    if (this.isConnected && !this._started) this.load();
  }

  set panel(value) { this._panel = value; }

  connectedCallback() {
    if (!this._started && this._hass) this.load();
    else if (!this._started) this.renderLoading();
  }

  t(key) { return TEXT[this.lang || "en"][key] || TEXT.en[key] || key; }

  async load() {
    this._started = true;
    this.renderLoading();
    try {
      this.data = await this._hass.callWS({ type: "network_inventory/list" });
      this.render();
    } catch (error) {
      this.renderError(error);
    }
  }

  renderLoading() {
    this.shadowRoot.innerHTML = `<style>${BASE_CSS}</style><div class="state"><div class="spinner"></div>${this.t("loading")}</div>`;
  }

  renderError(error) {
    this.shadowRoot.innerHTML = `<style>${BASE_CSS}</style><div class="state error">${esc(error?.message || this.t("error"))}</div>`;
  }

  render() {
    const content = this.view === "overview" ? this.renderOverview()
      : this.view === "devices" ? this.renderDevices()
      : this.view === "ha" ? this.renderHaDevices()
      : this.view === "unifi" ? this.renderUnifi()
      : this.view === "integrations" ? this.renderIntegrations()
      : this.renderSettings();
    this.shadowRoot.innerHTML = `
      <style>${BASE_CSS}</style>
      <div class="app">
        <header>
          <div><div class="title-row"><h1>${this.t("title")}</h1><span class="version">v${esc(this.data.version)}</span></div><p>${this.data.devices.length} ${this.t("devices").toLowerCase()}</p></div>
          <button class="primary" data-action="add"><ha-icon icon="mdi:plus"></ha-icon>${this.t("addDevice")}</button>
        </header>
        <nav>
          ${this.nav("overview", "mdi:view-dashboard-outline", "overview")}
          ${this.nav("devices", "mdi:devices", "devices")}
          ${this.nav("ha", "mdi:home-assistant", "homeAssistant", this.data.ha_devices.length)}
          ${this.data.integrations?.unifi?.connected ? this.nav("unifi", "mdi:access-point-network", "unifi", this.data.unifi_items.length) : ""}
          ${this.nav("integrations", "mdi:connection", "integrations")}
          ${this.nav("settings", "mdi:cog-outline", "settings")}
        </nav>
        <main>${content}</main>
        <div id="modal"></div><div id="toast"></div>
      </div>`;
    this.bindBaseEvents();
  }

  nav(view, icon, label, count = null) {
    return `<button class="nav ${this.view === view ? "active" : ""}" data-view="${view}"><ha-icon icon="${icon}"></ha-icon><span>${this.t(label)}</span>${count ? `<b>${count}</b>` : ""}</button>`;
  }

  renderOverview() {
    const devices = this.data.devices;
    const unique = key => new Set(devices.map(d => d[key]).filter(Boolean)).size;
    const groups = Object.entries(this.data.protocols).map(([key, p]) => ({
      key, ...p, count: devices.filter(d => d.protocol === key).length
    })).filter(item => item.count);
    const recent = [...devices].sort((a, b) => b.device_code - a.device_code).slice(0, 6);
    return `
      <section class="stats">
        ${this.stat("mdi:devices", this.t("total"), devices.length, "blue")}
        ${this.stat("mdi:floor-plan", this.t("areas"), unique("area"), "green")}
        ${this.stat("mdi:factory", this.t("brands"), unique("brand"), "orange")}
        ${this.stat("mdi:access-point-network", this.t("protocols"), groups.length, "purple")}
      </section>
      <section class="grid-two">
        <article class="card"><h2>${this.t("protocols")}</h2>
          <div class="protocol-list">${groups.length ? groups.map(g => `
            <div><span class="dot" style="background:${safeColor(g.color)}"></span><strong>${esc(g.label)}</strong><div class="bar"><i style="width:${Math.max(5, g.count / devices.length * 100)}%;background:${safeColor(g.color)}"></i></div><b>${g.count}</b></div>`).join("") : `<p class="muted">${this.t("empty")}</p>`}</div>
        </article>
        <article class="card"><h2>${this.t("devices")}</h2>${this.deviceMiniList(recent)}</article>
      </section>`;
  }

  stat(icon, label, value, color) {
    return `<article class="stat"><div class="stat-icon ${color}"><ha-icon icon="${icon}"></ha-icon></div><div><span>${label}</span><strong>${value}</strong></div></article>`;
  }

  deviceMiniList(devices) {
    if (!devices.length) return `<p class="muted">${this.t("empty")}</p>`;
    return `<div class="mini-list">${devices.map(d => `<button data-edit="${d.id}"><span class="code">${d.device_code}</span><span><strong>${esc(d.name)}</strong><small>${esc(d.area || d.brand || this.t("manual"))}</small></span><ha-icon icon="mdi:chevron-right"></ha-icon></button>`).join("")}</div>`;
  }

  renderDevices() {
    const protocolOptions = Object.entries(this.data.protocols).map(([key, p]) => `<option value="${esc(key)}" ${this.protocolFilter === key ? "selected" : ""}>${esc(p.label)}</option>`).join("");
    const option = (value, selected) => `<option value="${esc(value)}" ${selected === value ? "selected" : ""}>${esc(value)}</option>`;
    const typeOptions = this.data.device_types.map(value => option(value, this.typeFilter)).join("");
    const brandOptions = this.data.brands.map(value => option(value, this.brandFilter)).join("");
    const areas = [...new Set([...this.data.areas, ...this.data.devices.map(device => device.area).filter(Boolean)])].sort((a,b) => a.localeCompare(b));
    const areaOptions = areas.map(value => option(value, this.areaFilter)).join("");
    const devices = this.filteredDevices();
    return `
      <section class="toolbar card">
        <label class="search"><ha-icon icon="mdi:magnify"></ha-icon><input id="search" value="${esc(this.query)}" placeholder="${this.t("search")}"></label>
        <input type="file" id="csv-file" accept=".csv,text/csv" hidden>
        <button class="secondary" data-action="csv"><ha-icon icon="mdi:file-upload-outline"></ha-icon>${this.t("chooseCsv")}</button>
        <button class="secondary" data-action="export"><ha-icon icon="mdi:file-download-outline"></ha-icon>${this.t("exportCsv")}</button>
      </section>
      <section class="filters card">
        <select id="protocol-filter"><option value="">${this.t("allProtocols")}</option>${protocolOptions}</select>
        <select id="type-filter"><option value="">${this.t("allTypes")}</option>${typeOptions}</select>
        <select id="brand-filter"><option value="">${this.t("allBrands")}</option>${brandOptions}</select>
        <select id="area-filter"><option value="">${this.t("allAreas")}</option>${areaOptions}</select>
        <select id="status-filter"><option value="">${this.t("allStatuses")}</option><option value="online" ${this.statusFilter === "online" ? "selected" : ""}>Online</option><option value="offline" ${this.statusFilter === "offline" ? "selected" : ""}>Offline</option><option value="unknown" ${this.statusFilter === "unknown" ? "selected" : ""}>${this.t("unknown")}</option></select>
        <button class="secondary" data-action="clear-filters"><ha-icon icon="mdi:filter-off-outline"></ha-icon>${this.t("clearFilters")}</button>
      </section>
      <section class="table-card">
        <div class="table-scroll"><table><thead><tr>
          <th>${this.t("code")}</th><th>${this.t("name")}</th><th>${this.t("type")}</th><th>${this.t("brand")}</th>
          <th>${this.t("area")}</th><th>${this.t("address")}</th><th>${this.t("ip")}</th><th>${this.t("entityName")}</th><th>${this.t("protocol")}</th><th></th>
        </tr></thead><tbody>${devices.map(d => this.deviceRow(d)).join("")}</tbody></table></div>
        ${devices.length ? "" : `<div class="empty"><ha-icon icon="mdi:devices-off"></ha-icon><p>${this.t("empty")}</p></div>`}
      </section>`;
  }

  deviceRow(d) {
    const protocol = this.data.protocols[d.protocol] || { label: d.protocol, color: "#64748b" };
    const unifi = this.data.unifi_matches?.[d.id];
    return `<tr>
      <td><span class="code">${d.device_code}</span></td>
      <td><div class="device-name"><strong>${esc(d.name)}</strong>${unifi ? `<button class="unifi-badge" data-unifi-details="${esc(d.id)}" title="${this.t("unifiBadge")}"><ha-icon icon="mdi:access-point-network"></ha-icon>UniFi</button>` : ""}</div><small>${esc(d.model || d.integration || "")}</small></td>
      <td>${esc(d.device_type)}</td><td>${esc(d.brand)}</td><td>${esc(d.area)}</td>
      <td class="mono">${esc(d.mac)}</td><td class="mono">${esc(d.ip_address)}</td><td class="mono">${esc(d.entity_name)}</td>
      <td><span class="pill" style="--pill:${safeColor(protocol.color)}">${esc(protocol.label)}</span></td>
      <td><div class="row-actions"><button title="${this.t("edit")}" data-edit="${d.id}"><ha-icon icon="mdi:pencil-outline"></ha-icon></button><button class="danger-icon" title="${this.t("delete")}" data-delete="${d.id}"><ha-icon icon="mdi:delete-outline"></ha-icon></button></div></td>
    </tr>`;
  }

  renderHaDevices() {
    const devices = this.data.ha_devices;
    return `<section class="section-head"><div><h2>${this.t("homeAssistant")}</h2><p>${this.t("importHa")}</p></div></section>
      <section class="import-grid">${devices.map((d, index) => {
        const p = this.data.protocols[d.protocol] || this.data.protocols.other;
        return `<article class="import-card"><div class="device-icon"><ha-icon icon="mdi:devices"></ha-icon></div><div class="grow"><h3>${esc(d.name)}</h3><p>${esc([d.brand, d.model].filter(Boolean).join(" · "))}</p><div class="meta"><span>${esc(d.area || "—")}</span><span>${esc(d.integration || "—")}</span><span class="pill" style="--pill:${safeColor(p.color)}">${esc(p.label)}</span></div></div><button class="primary compact" data-import="${index}">${this.t("import")}</button></article>`;
      }).join("")}</section>${devices.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:check-circle-outline"></ha-icon><p>${this.t("noHa")}</p></div>`}`;
  }

  renderIntegrations() {
    const state = this.data.integrations?.unifi || {};
    const options = (state.available_sites || []).map(site => `<option value="${esc(`${site.host_id}|${site.site_id}`)}">${esc(site.name)} · ${esc(site.gateway_mac || site.site_id)}</option>`).join("");
    return `<section class="section-head"><div><h2>${this.t("integrations")}</h2><p>${this.t("unifiHelp")}</p></div></section>
      <article class="card integration-card">
        <div class="integration-logo"><ha-icon icon="mdi:access-point-network"></ha-icon></div>
        <div class="grow"><div class="integration-title"><h2>${this.t("unifiCloud")}</h2><span class="status-dot ${state.connected ? "ok" : ""}">${state.connected ? this.t("connected") : this.t("notConnected")}</span></div>
          <p class="muted">${state.connected ? esc(state.site_name) : this.t("unifiHelp")}</p>
          ${state.last_error ? `<p class="inline-error">${esc(state.last_error)}</p>` : ""}
          ${state.configured && !state.connected && options ? `<form id="unifi-site-form" class="inline-form"><label>${this.t("selectSite")}<select name="site" required><option value=""></option>${options}</select></label><button class="primary" type="submit">${this.t("connect")}</button></form><p class="muted">${this.t("chooseSiteHelp")}</p>` : ""}
          ${!state.configured ? `<form id="unifi-connect-form" class="inline-form"><label>${this.t("apiKey")}<input name="api_key" type="password" autocomplete="new-password" placeholder="${this.t("apiKeyPlaceholder")}" required></label><button class="primary" type="submit">${this.t("connect")}</button></form>` : ""}
          <a class="doc-link" href="https://unifi.ui.com/settings/api-keys" target="_blank" rel="noopener noreferrer">${this.t("createKey")} <ha-icon icon="mdi:open-in-new"></ha-icon></a>
        </div>
        ${state.connected ? `<div class="integration-actions"><button class="secondary" data-action="unifi-refresh"><ha-icon icon="mdi:refresh"></ha-icon>${this.t("refresh")}</button><button class="secondary danger-text" data-action="unifi-disconnect"><ha-icon icon="mdi:link-off"></ha-icon>${this.t("disconnect")}</button></div>` : state.configured ? `<button class="secondary danger-text" data-action="unifi-disconnect"><ha-icon icon="mdi:delete-outline"></ha-icon>${this.t("disconnect")}</button>` : ""}
      </article>`;
  }

  renderUnifi() {
    const items = this.data.unifi_items || [];
    const state = this.data.integrations?.unifi || {};
    return `<section class="section-head"><div><h2>${this.t("unifi")}</h2><p>${this.t("activeClients")} · ${esc(state.site_name || "")}</p></div><button class="secondary" data-action="unifi-refresh"><ha-icon icon="mdi:refresh"></ha-icon>${this.t("refresh")}</button></section>
      <section class="import-grid">${items.map((item, index) => {
        const p = this.data.protocols[item.protocol] || this.data.protocols.other;
        return `<article class="import-card"><div class="device-icon unifi-icon"><ha-icon icon="${item.kind === "infrastructure" ? "mdi:access-point-network" : item.protocol === "wifi" ? "mdi:wifi" : "mdi:ethernet"}"></ha-icon></div><div class="grow"><h3>${esc(item.name)}</h3><p>${esc([item.ip_address, item.mac].filter(Boolean).join(" · "))}</p><div class="meta"><span>${esc(item.connection_type || "—")}</span>${item.uplink_name ? `<span>${this.t("uplink")}: ${esc(item.uplink_name)}</span>` : ""}<span class="pill" style="--pill:${safeColor(p.color)}">${esc(p.label)}</span></div></div>${item.inventory_id ? `<button class="secondary compact" data-unifi-details-inventory="${esc(item.inventory_id)}"><ha-icon icon="mdi:check"></ha-icon>${this.t("added")}</button>` : `<button class="primary compact" data-unifi-import="${index}">${this.t("import")}</button>`}</article>`;
      }).join("")}</section>${items.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:lan-disconnect"></ha-icon><p>${this.t("noUnifi")}</p></div>`}`;
  }

  renderSettings() {
    const rows = Object.entries(this.data.protocols).map(([key, p]) => this.protocolRow(key, p)).join("");
    return `<form id="settings-form">
      <section class="card settings-card"><div class="section-head"><div><h2>${this.t("ranges")}</h2><p>${this.t("rangeHelp")}</p></div><button type="button" class="secondary" data-action="add-protocol"><ha-icon icon="mdi:plus"></ha-icon>${this.t("addProtocol")}</button></div>
        <div id="protocol-rows" class="protocol-settings">${rows}</div>
      </section>
      <section class="card settings-card"><h2>${this.t("deviceTypes")}</h2><textarea id="device-types" rows="12">${esc(this.data.device_types.join("\n"))}</textarea></section>
      <section class="card settings-card"><h2>${this.t("brandSettings")}</h2><textarea id="brands" rows="8">${esc(this.data.brands.join("\n"))}</textarea></section>
      <div class="form-actions"><button type="submit" class="primary"><ha-icon icon="mdi:content-save-outline"></ha-icon>${this.t("saveSettings")}</button></div>
    </form>`;
  }

  protocolRow(key = "", p = { label: "", start: "", end: "", color: "#64748b" }) {
    return `<div class="protocol-setting">
      <label>${this.t("key")}<input name="key" value="${esc(key)}" ${key ? "readonly" : ""} required pattern="[a-z0-9_-]+"></label>
      <label>${this.t("name")}<input name="label" value="${esc(p.label)}" required></label>
      <label>${this.t("start")}<input name="start" type="number" min="1" value="${esc(p.start)}" required></label>
      <label>${this.t("end")}<input name="end" type="number" min="1" value="${esc(p.end)}" required></label>
      <label>${this.t("color")}<input name="color" type="color" value="${safeColor(p.color)}"></label>
      <button type="button" class="danger-icon" data-remove-protocol><ha-icon icon="mdi:close"></ha-icon></button>
    </div>`;
  }

  bindBaseEvents() {
    this.shadowRoot.querySelectorAll("[data-view]").forEach(button => button.addEventListener("click", () => {
      this.view = button.dataset.view; this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-action='add']").forEach(button => button.addEventListener("click", () => this.openDeviceModal()));
    this.shadowRoot.querySelectorAll("[data-edit]").forEach(button => button.addEventListener("click", () => {
      const device = this.data.devices.find(item => item.id === button.dataset.edit); if (device) this.openDeviceModal(device);
    }));
    this.shadowRoot.querySelectorAll("[data-delete]").forEach(button => button.addEventListener("click", () => this.deleteDevice(button.dataset.delete)));
    this.shadowRoot.querySelector("#search")?.addEventListener("input", event => { this.query = event.target.value; this.refreshDeviceBody(); });
    [["protocol", "protocolFilter"], ["type", "typeFilter"], ["brand", "brandFilter"], ["area", "areaFilter"], ["status", "statusFilter"]].forEach(([id, property]) => {
      this.shadowRoot.querySelector(`#${id}-filter`)?.addEventListener("change", event => { this[property] = event.target.value; this.render(); });
    });
    this.shadowRoot.querySelector("[data-action='clear-filters']")?.addEventListener("click", () => {
      this.protocolFilter = this.typeFilter = this.brandFilter = this.areaFilter = this.statusFilter = "";
      this.query = "";
      this.render();
    });
    this.shadowRoot.querySelector("[data-action='export']")?.addEventListener("click", () => this.exportCsv());
    this.shadowRoot.querySelector("[data-action='csv']")?.addEventListener("click", () => this.shadowRoot.querySelector("#csv-file").click());
    this.shadowRoot.querySelector("#csv-file")?.addEventListener("change", event => this.importCsv(event.target.files[0]));
    this.shadowRoot.querySelectorAll("[data-import]").forEach(button => button.addEventListener("click", () => this.openDeviceModal(this.data.ha_devices[Number(button.dataset.import)], true)));
    this.shadowRoot.querySelectorAll("[data-unifi-import]").forEach(button => button.addEventListener("click", () => this.openDeviceModal(this.unifiImportDevice(this.data.unifi_items[Number(button.dataset.unifiImport)]), true)));
    this.shadowRoot.querySelectorAll("[data-unifi-details]").forEach(button => button.addEventListener("click", () => this.openUnifiDetails(this.data.unifi_matches[button.dataset.unifiDetails])));
    this.shadowRoot.querySelectorAll("[data-unifi-details-inventory]").forEach(button => button.addEventListener("click", () => this.openUnifiDetails(this.data.unifi_matches[button.dataset.unifiDetailsInventory])));
    this.shadowRoot.querySelector("#unifi-connect-form")?.addEventListener("submit", event => this.connectUnifi(event));
    this.shadowRoot.querySelector("#unifi-site-form")?.addEventListener("submit", event => this.selectUnifiSite(event));
    this.shadowRoot.querySelectorAll("[data-action='unifi-refresh']").forEach(button => button.addEventListener("click", () => this.refreshUnifi(button)));
    this.shadowRoot.querySelectorAll("[data-action='unifi-disconnect']").forEach(button => button.addEventListener("click", () => this.disconnectUnifi(button)));
    this.shadowRoot.querySelector("[data-action='add-protocol']")?.addEventListener("click", () => this.addProtocolRow());
    this.shadowRoot.querySelectorAll("[data-remove-protocol]").forEach(button => button.addEventListener("click", () => button.closest(".protocol-setting").remove()));
    this.shadowRoot.querySelector("#settings-form")?.addEventListener("submit", event => this.saveSettings(event));
  }

  refreshDeviceBody() {
    const tbody = this.shadowRoot.querySelector("tbody");
    if (!tbody) return;
    const devices = this.filteredDevices();
    tbody.innerHTML = devices.map(d => this.deviceRow(d)).join("");
    tbody.querySelectorAll("[data-edit]").forEach(b => b.addEventListener("click", () => this.openDeviceModal(this.data.devices.find(d => d.id === b.dataset.edit))));
    tbody.querySelectorAll("[data-delete]").forEach(b => b.addEventListener("click", () => this.deleteDevice(b.dataset.delete)));
    tbody.querySelectorAll("[data-unifi-details]").forEach(b => b.addEventListener("click", () => this.openUnifiDetails(this.data.unifi_matches[b.dataset.unifiDetails])));
  }

  unifiImportDevice(item) {
    return {
      ...item,
      area: "",
      integration: "unifi",
      device_identifier: `unifi:${item.id}`,
      entity_name: "",
      comments: item.uplink_name ? `${this.t("uplink")}: ${item.uplink_name}` : "",
      unifi_id: item.id,
      unifi_kind: item.kind,
      unifi_site_id: this.data.integrations?.unifi?.site_id || ""
    };
  }

  async connectUnifi(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const api_key = new FormData(form).get("api_key");
    this.setBusy(form, true);
    try {
      await this._hass.callWS({ type: "network_inventory/unifi/connect", api_key });
      await this.reload(this.t("saved"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  async selectUnifiSite(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const selectedSite = String(new FormData(form).get("site") || "");
    const [host_id, site_id] = selectedSite.split("|");
    if (!host_id || !site_id) return;
    this.setBusy(form, true);
    try {
      await this._hass.callWS({ type: "network_inventory/unifi/connect", host_id, site_id });
      this.view = "unifi";
      await this.reload(this.t("saved"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  async refreshUnifi(button) {
    button.disabled = true;
    try { await this._hass.callWS({ type: "network_inventory/unifi/refresh" }); await this.reload(this.t("saved")); }
    catch (error) { this.toast(error?.message || this.t("error"), true); button.disabled = false; }
  }

  async disconnectUnifi(button) {
    button.disabled = true;
    try {
      await this._hass.callWS({ type: "network_inventory/unifi/disconnect" });
      this.view = "integrations";
      await this.reload(this.t("saved"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); button.disabled = false; }
  }

  openUnifiDetails(item) {
    if (!item) return;
    const modal = this.shadowRoot.querySelector("#modal");
    const rows = [
      [this.t("name"), item.name], [this.t("address"), item.mac], [this.t("ip"), item.ip_address],
      [this.t("type"), item.connection_type], [this.t("model"), item.model], [this.t("firmware"), item.firmware_version],
      [this.t("uplink"), [item.uplink_name, item.uplink_model, item.uplink_ip].filter(Boolean).join(" · ")],
      [this.t("connectedSince"), formatDate(item.connected_at)]
    ].filter(([, value]) => value);
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal details-modal"><div class="modal-head"><div><h2>${esc(item.name)}</h2><p>UniFi · ${esc(item.connection_type || item.kind)}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div><div class="detail-list">${rows.map(([label, value]) => `<div><span>${esc(label)}</span><strong>${esc(value)}</strong></div>`).join("")}</div></section></div>`;
    modal.querySelector("[data-close]").addEventListener("click", () => modal.innerHTML = "");
  }

  filteredDevices() {
    const q = this.query.toLowerCase();
    return [...this.data.devices].filter(device =>
      (!this.protocolFilter || device.protocol === this.protocolFilter) &&
      (!this.typeFilter || device.device_type === this.typeFilter) &&
      (!this.brandFilter || device.brand === this.brandFilter) &&
      (!this.areaFilter || device.area === this.areaFilter) &&
      (!this.statusFilter || device.status === this.statusFilter) &&
      (!q || Object.values(device).join(" ").toLowerCase().includes(q))
    ).sort((a,b) => a.device_code-b.device_code);
  }

  openDeviceModal(device = null, isImport = false) {
    const protocols = Object.entries(this.data.protocols).map(([key,p]) => `<option value="${esc(key)}" ${(device?.protocol || "wifi") === key ? "selected" : ""}>${esc(p.label)}</option>`).join("");
    const types = this.data.device_types.map(type => `<option value="${esc(type)}" ${device?.device_type === type ? "selected" : ""}>${esc(type)}</option>`).join("");
    const brands = [...this.data.brands];
    if (device?.brand && !brands.some(brand => brand.toLowerCase() === device.brand.toLowerCase())) brands.push(device.brand);
    const brandOptions = brands.sort((a,b) => a.localeCompare(b)).map(brand => `<option value="${esc(brand)}" ${device?.brand === brand ? "selected" : ""}>${esc(brand)}</option>`).join("");
    const areaOptions = this.data.areas.map(area => `<option value="${esc(area)}"></option>`).join("");
    const isEdit = Boolean(device && !isImport);
    const ipRequired = ["wifi", "ethernet"].includes(device?.protocol || "wifi");
    const modal = this.shadowRoot.querySelector("#modal");
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal"><div class="modal-head"><div><h2>${isEdit ? this.t("edit") : this.t("addDevice")}</h2><p>${isEdit ? `${this.t("code")}: ${device.device_code}` : this.t("autoId")}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div>
      <form id="device-form"><div class="form-grid">
        ${isEdit ? `<label>${this.t("code")}<div class="id-field"><input name="device_code" value="${esc(device.device_code)}" readonly><button type="button" class="secondary" data-clear-id title="${this.t("clearId")}"><ha-icon icon="mdi:close"></ha-icon></button></div><small data-id-help></small></label>` : ""}
        ${field("name", this.t("name"), device?.name, true)}
        <label>${this.t("type")}<select name="device_type" required><option value=""></option>${types}</select></label>
        <label>${this.t("brand")}<select name="brand" required><option value=""></option>${brandOptions}</select></label>${field("model", this.t("model"), device?.model)}
        <label>${this.t("area")}<input name="area" list="area-options" value="${esc(device?.area || "")}" required><datalist id="area-options">${areaOptions}</datalist></label>
        <label>${this.t("protocol")}<select name="protocol" required>${protocols}</select><small>${isEdit ? this.t("stableId") : ""}</small></label>
        ${field("mac", this.t("address"), device?.mac, true)}${field("ip_address", this.t("ip"), device?.ip_address, ipRequired)}
        ${field("device_identifier", this.t("identifier"), device?.device_identifier)}${field("entity_name", this.t("entityName"), device?.entity_name)}
        ${field("integration", this.t("integration"), device?.integration)}
        <label>${this.t("status")}<select name="status"><option value="unknown">${this.t("unknown")}</option><option value="online" ${device?.status === "online" ? "selected" : ""}>Online</option><option value="offline" ${device?.status === "offline" ? "selected" : ""}>Offline</option></select></label>
        <label class="full">${this.t("comments")}<textarea name="comments" rows="3">${esc(device?.comments || "")}</textarea></label>
      </div><div class="modal-actions"><button type="button" class="secondary" data-close>${this.t("cancel")}</button><button type="submit" class="primary">${this.t("save")}</button></div></form></section></div>`;
    modal.querySelectorAll("[data-close]").forEach(button => button.addEventListener("click", () => modal.innerHTML = ""));
    const protocolSelect = modal.querySelector("[name='protocol']");
    const ipInput = modal.querySelector("[name='ip_address']");
    protocolSelect.addEventListener("change", () => { ipInput.required = ["wifi", "ethernet"].includes(protocolSelect.value); });
    modal.querySelector("[data-clear-id]")?.addEventListener("click", () => {
      modal.querySelector("[name='device_code']").value = "";
      modal.querySelector("[data-id-help]").textContent = this.t("newIdHelp");
    });
    modal.querySelector("#device-form").addEventListener("submit", event => this.saveDevice(event, isEdit ? device : null, isImport ? device : null));
  }

  async saveDevice(event, existing, importSource = null) {
    event.preventDefault();
    const form = event.currentTarget;
    const payload = Object.fromEntries(new FormData(form).entries());
    if (!payload.name.trim()) return this.toast(this.t("requiredName"), true);
    this.setBusy(form, true);
    try {
      let message = this.t("saved");
      if (importSource) {
        const result = await this._hass.callWS({ type: "network_inventory/import", devices: [{ ...importSource, ...payload }] });
        message = `${result.imported} ${this.t("imported")}, ${result.skipped} ${this.t("skipped")}`;
      } else {
        await this._hass.callWS({ type: existing ? "network_inventory/update" : "network_inventory/add", ...(existing ? { device_id: existing.id } : {}), device: payload });
      }
      this.shadowRoot.querySelector("#modal").innerHTML = "";
      await this.reload(message);
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  async deleteDevice(id) {
    if (!confirm(this.t("confirmDelete"))) return;
    try { await this._hass.callWS({ type: "network_inventory/delete", device_id: id }); await this.reload(this.t("saved")); }
    catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async importCsv(file) {
    if (!file) return;
    try {
      const rows = csvToDevices(await file.text());
      const result = await this._hass.callWS({ type: "network_inventory/import", devices: rows });
      await this.reload(`${result.imported} ${this.t("imported")}, ${result.skipped} ${this.t("skipped")}`);
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  exportCsv() {
    const headers = ["Device Code","MAC / IEEE Address","Device IP","Device Type","Brand","Area","Device Name","Device ID","Entity Name","Comments","Protocol"];
    const keys = ["device_code","mac","ip_address","device_type","brand","area","name","device_identifier","entity_name","comments","protocol"];
    const lines = [headers, ...this.data.devices.sort((a,b) => a.device_code-b.device_code).map(d => keys.map(k => d[k] ?? ""))];
    const csv = lines.map(row => row.map(csvCell).join(",")).join("\r\n");
    const link = document.createElement("a");
    link.href = URL.createObjectURL(new Blob(["\ufeff" + csv], { type: "text/csv;charset=utf-8" }));
    link.download = `network-inventory-${new Date().toISOString().slice(0,10)}.csv`;
    link.click(); URL.revokeObjectURL(link.href);
  }

  addProtocolRow() {
    const container = this.shadowRoot.querySelector("#protocol-rows");
    container.insertAdjacentHTML("beforeend", this.protocolRow());
    container.lastElementChild.querySelector("[data-remove-protocol]").addEventListener("click", event => event.currentTarget.closest(".protocol-setting").remove());
  }

  async saveSettings(event) {
    event.preventDefault();
    const protocols = {};
    this.shadowRoot.querySelectorAll(".protocol-setting").forEach(row => {
      const values = Object.fromEntries(new FormData(wrapForm(row)).entries());
      protocols[values.key] = { label: values.label, start: Number(values.start), end: Number(values.end), color: values.color };
    });
    const device_types = this.shadowRoot.querySelector("#device-types").value.split("\n").map(v => v.trim()).filter(Boolean);
    const brands = this.shadowRoot.querySelector("#brands").value.split("\n").map(v => v.trim()).filter(Boolean);
    try { await this._hass.callWS({ type: "network_inventory/settings", settings: { protocols, device_types, brands } }); await this.reload(this.t("saved")); }
    catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async reload(message) {
    this.data = await this._hass.callWS({ type: "network_inventory/list" });
    this.render(); this.toast(message);
  }

  toast(message, error = false) {
    const target = this.shadowRoot.querySelector("#toast");
    if (!target) return;
    target.textContent = message; target.className = error ? "show error" : "show";
    clearTimeout(this._toastTimer); this._toastTimer = setTimeout(() => target.className = "", 3200);
  }

  setBusy(form, busy) { form.querySelectorAll("button,input,select,textarea").forEach(el => el.disabled = busy); }
}

function field(name, label, value = "", required = false) {
  return `<label>${label}<input name="${name}" value="${esc(value || "")}" ${required ? "required" : ""}></label>`;
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"]/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[char]);
}

function safeColor(value) { return /^#[0-9a-f]{6}$/i.test(value || "") ? value : "#64748b"; }
function formatDate(value) { if (!value) return ""; const date = new Date(value); return Number.isNaN(date.getTime()) ? value : date.toLocaleString(); }
function csvCell(value) { const text = String(value ?? ""); return /[",\r\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text; }
function wrapForm(node) { const form = document.createElement("form"); [...node.querySelectorAll("input,select,textarea")].forEach(el => form.append(el.cloneNode(true))); return form; }

function parseCsv(text) {
  const rows = []; let row = [], cell = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (quoted && char === '"' && text[i + 1] === '"') { cell += '"'; i++; }
    else if (char === '"') quoted = !quoted;
    else if (char === "," && !quoted) { row.push(cell); cell = ""; }
    else if ((char === "\n" || char === "\r") && !quoted) {
      if (char === "\r" && text[i + 1] === "\n") i++;
      row.push(cell); if (row.some(value => value.trim())) rows.push(row); row = []; cell = "";
    } else cell += char;
  }
  row.push(cell); if (row.some(value => value.trim())) rows.push(row);
  return rows;
}

function csvToDevices(text) {
  const rows = parseCsv(text.replace(/^\ufeff/, ""));
  if (rows.length < 2) throw new Error("The CSV file has no device rows.");
  const normalise = value => String(value || "").toLowerCase().replace(/[^a-z0-9]+/g, "");
  const headers = rows[0].map(normalise);
  const find = (...names) => headers.findIndex(header => names.includes(header));
  const index = {
    device_code: find("devicecode", "code"), mac: find("macieeeaddress", "macaddress", "mac", "ieee"),
    ip_address: find("deviceip", "ipaddress", "ip"), device_type: find("devicetype", "type"), brand: find("brand", "manufacturer"),
    area: find("area", "room"), name: find("devicename", "name"), device_identifier: find("deviceid", "identifier"),
    entity_name: find("entityname"),
    comments: find("comments", "notes"), protocol: find("protocol", "connection", "network")
  };
  if (index.protocol < 0 && rows[0].length >= 10) index.protocol = rows[0].length - 1;
  return rows.slice(1).map(row => Object.fromEntries(Object.entries(index).map(([key, i]) => [key, i >= 0 ? (row[i] || "").trim() : ""]))).filter(item => item.name);
}

const BASE_CSS = `
  :host{display:block;min-height:100%;background:var(--primary-background-color);color:var(--primary-text-color);font-family:var(--paper-font-body1_-_font-family,system-ui,sans-serif)}
  *{box-sizing:border-box}button,input,select,textarea{font:inherit;color:inherit}button{cursor:pointer}.app{max-width:1500px;margin:auto;padding:24px 28px 60px}header{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:22px}h1{font-size:28px;margin:0 0 3px;letter-spacing:-.4px}h2{font-size:18px;margin:0 0 18px}h3{font-size:15px;margin:0 0 5px}p{margin:0}header p,.section-head p,.muted{color:var(--secondary-text-color);font-size:13px}
  .title-row{display:flex;align-items:center;gap:9px}.version{font-size:11px;font-weight:700;color:var(--secondary-text-color);border:1px solid var(--divider-color);border-radius:20px;padding:3px 7px}
  button{border:0;background:none}.primary,.secondary{height:42px;border-radius:10px;padding:0 15px;display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:650;white-space:nowrap}.primary{background:var(--primary-color);color:#fff}.secondary{border:1px solid var(--divider-color);background:var(--card-background-color)}.compact{height:36px;padding:0 12px;font-size:13px}button:disabled{opacity:.55;cursor:wait}
  nav{display:flex;gap:5px;border-bottom:1px solid var(--divider-color);margin-bottom:24px;overflow:auto}.nav{padding:12px 15px;display:flex;align-items:center;gap:8px;color:var(--secondary-text-color);border-bottom:2px solid transparent;white-space:nowrap}.nav.active{color:var(--primary-color);border-color:var(--primary-color);font-weight:650}.nav b{font-size:11px;background:var(--primary-color);color:#fff;border-radius:20px;padding:2px 6px}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.stat,.card,.table-card,.import-card{background:var(--card-background-color);border:1px solid var(--divider-color);border-radius:14px}.stat{padding:18px;display:flex;align-items:center;gap:14px}.stat-icon{width:44px;height:44px;border-radius:12px;display:grid;place-items:center}.stat-icon.blue{background:#dbeafe;color:#2563eb}.stat-icon.green{background:#d1fae5;color:#059669}.stat-icon.orange{background:#ffedd5;color:#ea580c}.stat-icon.purple{background:#ede9fe;color:#7c3aed}.stat span{display:block;font-size:12px;color:var(--secondary-text-color);margin-bottom:3px}.stat strong{font-size:24px}.grid-two{display:grid;grid-template-columns:1fr 1.3fr;gap:16px}.card{padding:20px}.protocol-list>div{display:grid;grid-template-columns:10px 90px 1fr 28px;align-items:center;gap:9px;margin:14px 0;font-size:13px}.dot{width:9px;height:9px;border-radius:50%}.bar{height:7px;background:var(--divider-color);border-radius:10px;overflow:hidden}.bar i{display:block;height:100%;border-radius:10px}.mini-list button{width:100%;display:grid;grid-template-columns:58px 1fr 24px;align-items:center;text-align:left;padding:10px 5px;border-bottom:1px solid var(--divider-color)}.mini-list button:last-child{border:0}.mini-list small,td small{display:block;color:var(--secondary-text-color);margin-top:3px}.code{font-family:ui-monospace,monospace;font-weight:750;color:var(--primary-color)}
  .toolbar{display:flex;gap:10px;margin-bottom:10px;padding:12px}.filters{display:grid;grid-template-columns:repeat(5,minmax(120px,1fr)) auto;gap:10px;margin-bottom:14px;padding:12px}.search{flex:1;min-width:190px;display:flex;align-items:center;gap:8px;border:1px solid var(--divider-color);border-radius:9px;padding:0 11px}.search input{border:0;background:transparent;width:100%;outline:0;height:40px}select,input,textarea{border:1px solid var(--divider-color);background:var(--card-background-color);border-radius:8px;padding:10px;outline:none}select:focus,input:focus,textarea:focus{border-color:var(--primary-color);box-shadow:0 0 0 2px color-mix(in srgb,var(--primary-color) 18%,transparent)}.table-card{overflow:hidden}.table-scroll{overflow:auto}table{width:100%;border-collapse:collapse;font-size:13px}th{text-align:left;color:var(--secondary-text-color);font-size:11px;text-transform:uppercase;letter-spacing:.35px;background:var(--secondary-background-color);padding:12px}td{padding:12px;border-top:1px solid var(--divider-color);white-space:nowrap}.mono{font-family:ui-monospace,monospace;font-size:12px}.pill{display:inline-flex;border-radius:20px;padding:4px 9px;background:color-mix(in srgb,var(--pill) 14%,transparent);color:var(--pill);font-size:12px;font-weight:650}.row-actions{display:flex}.row-actions button,.modal-head button,.danger-icon{width:36px;height:36px;border-radius:8px;display:grid;place-items:center}.row-actions button:hover,.modal-head button:hover{background:var(--secondary-background-color)}.danger-icon{color:var(--error-color,#dc2626)}
  .section-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px}.section-head h2{margin:0 0 4px}.import-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.import-card{padding:15px;display:flex;align-items:center;gap:13px}.device-icon{width:42px;height:42px;border-radius:11px;background:var(--secondary-background-color);display:grid;place-items:center;color:var(--primary-color)}.unifi-icon{background:#e0f2fe;color:#0284c7}.grow{flex:1;min-width:0}.import-card p{font-size:12px;color:var(--secondary-text-color);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.meta{display:flex;gap:7px;margin-top:8px;align-items:center;flex-wrap:wrap}.meta>span:not(.pill){font-size:11px;color:var(--secondary-text-color)}.empty{padding:50px;text-align:center;color:var(--secondary-text-color)}.empty ha-icon{--mdc-icon-size:42px;margin-bottom:10px}.standalone{background:var(--card-background-color);border-radius:14px}
  .device-name{display:flex;align-items:center;gap:7px}.unifi-badge{display:inline-flex;align-items:center;gap:3px;border-radius:20px;padding:3px 7px;background:#e0f2fe;color:#0369a1;font-size:10px;font-weight:750}.unifi-badge ha-icon{--mdc-icon-size:13px}.integration-card{display:flex;align-items:flex-start;gap:16px}.integration-logo{width:54px;height:54px;flex:0 0 54px;border-radius:14px;background:#e0f2fe;color:#0284c7;display:grid;place-items:center}.integration-logo ha-icon{--mdc-icon-size:30px}.integration-title{display:flex;align-items:center;gap:10px}.integration-title h2{margin:0}.status-dot{font-size:11px;font-weight:700;padding:4px 8px;border-radius:20px;background:var(--secondary-background-color);color:var(--secondary-text-color)}.status-dot.ok{background:#d1fae5;color:#047857}.inline-form{display:flex;align-items:end;gap:10px;margin:16px 0 8px}.inline-form label{display:grid;gap:6px;flex:1;max-width:520px;font-size:12px;color:var(--secondary-text-color)}.inline-form input,.inline-form select{width:100%}.doc-link{display:inline-flex;align-items:center;gap:5px;color:var(--primary-color);font-size:12px;margin-top:12px;text-decoration:none}.doc-link ha-icon{--mdc-icon-size:14px}.integration-actions{display:flex;gap:8px}.danger-text{color:var(--error-color,#c62828)}.inline-error{color:var(--error-color,#c62828);font-size:12px;margin-top:8px}.details-modal{width:min(600px,100%)}.detail-list{padding:8px 20px 22px}.detail-list>div{display:grid;grid-template-columns:150px 1fr;gap:15px;padding:12px 0;border-bottom:1px solid var(--divider-color)}.detail-list span{font-size:12px;color:var(--secondary-text-color)}.detail-list strong{font-size:13px;overflow-wrap:anywhere}
  .settings-card{margin-bottom:14px}.protocol-settings{display:grid;gap:10px}.protocol-setting{display:grid;grid-template-columns:1fr 1.3fr .7fr .7fr .55fr 40px;gap:10px;align-items:end;padding:12px;border:1px solid var(--divider-color);border-radius:10px}.protocol-setting label,.form-grid label{font-size:12px;color:var(--secondary-text-color);display:grid;gap:6px}.protocol-setting input{width:100%}.protocol-setting input[type=color]{height:41px;padding:5px}.settings-card textarea{width:100%;resize:vertical}.form-actions{display:flex;justify-content:flex-end}
  .modal-backdrop{position:fixed;z-index:20;inset:0;background:#0008;display:grid;place-items:center;padding:18px}.modal{width:min(760px,100%);max-height:92vh;overflow:auto;background:var(--card-background-color);border-radius:16px;box-shadow:0 20px 70px #0006}.modal-head{padding:19px 21px;border-bottom:1px solid var(--divider-color);display:flex;justify-content:space-between}.modal-head h2{margin:0 0 4px}.modal-head p{font-size:12px;color:var(--secondary-text-color)}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:20px}.form-grid input,.form-grid select,.form-grid textarea{width:100%}.form-grid .full{grid-column:1/-1}.form-grid small{min-height:13px}.id-field{display:grid;grid-template-columns:1fr 42px;gap:7px}.id-field button{width:42px;padding:0}.modal-actions{padding:15px 20px;border-top:1px solid var(--divider-color);display:flex;justify-content:flex-end;gap:9px}#toast{position:fixed;z-index:30;left:50%;bottom:30px;transform:translate(-50%,30px);background:#17202a;color:#fff;padding:11px 16px;border-radius:9px;opacity:0;pointer-events:none;transition:.2s}#toast.show{opacity:1;transform:translate(-50%,0)}#toast.error{background:var(--error-color,#c62828)}.state{min-height:70vh;display:flex;align-items:center;justify-content:center;gap:12px;color:var(--secondary-text-color)}.spinner{width:22px;height:22px;border:3px solid var(--divider-color);border-top-color:var(--primary-color);border-radius:50%;animation:spin .8s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
  @media(max-width:900px){.stats{grid-template-columns:repeat(2,1fr)}.grid-two,.import-grid{grid-template-columns:1fr}.toolbar{flex-wrap:wrap}.search{flex-basis:100%}.filters{grid-template-columns:repeat(2,minmax(0,1fr))}.protocol-setting{grid-template-columns:1fr 1fr 1fr}.protocol-setting .danger-icon{align-self:end}.app{padding:18px 14px 50px}.integration-card{flex-wrap:wrap}.integration-actions{width:100%;justify-content:flex-end}}
  @media(max-width:600px){header{align-items:flex-start}header h1{font-size:22px}header .primary{font-size:0;width:42px;padding:0}header .primary ha-icon{font-size:initial}.stats{gap:9px}.stat{padding:13px;gap:10px}.stat-icon{width:38px;height:38px}.stat strong{font-size:20px}.nav{padding:11px 12px}.nav span{font-size:12px}.toolbar .secondary{flex:1;font-size:12px;padding:0 8px}.filters{grid-template-columns:1fr}.form-grid{grid-template-columns:1fr}.form-grid .full{grid-column:auto}.protocol-setting{grid-template-columns:1fr 1fr}.import-card{align-items:flex-start}.import-card .primary{align-self:center}.section-head{align-items:flex-start}.section-head .secondary{font-size:0;width:42px;padding:0}.section-head .secondary ha-icon{font-size:initial}.inline-form{align-items:stretch;flex-direction:column}.inline-form button{width:100%}.detail-list>div{grid-template-columns:1fr;gap:4px}}
`;

customElements.define("network-inventory-panel", NetworkInventoryPanel);
