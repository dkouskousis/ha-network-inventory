const TEXT = {
  en: {
    title: "Network Inventory", overview: "Overview", devices: "Devices", newestDevices: "Newest Devices", discover: "Discover", homeAssistant: "Home Assistant",
    settings: "Settings", integrations: "Integrations", logs: "Logs", addDevice: "Add device", total: "Total devices", areas: "Areas", brands: "Brands",
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
    apiKeyPlaceholder: "Paste the UniFi API key", unifiBadge: "View UniFi connection details",
    allIpIssues: "All IP checks", ipMismatch: "Inventory / UniFi mismatch", duplicateIp: "Duplicate IP",
    unifiIp: "UniFi IP", inventoryIp: "Inventory IP", updateInventoryIp: "Update Inventory IP", addInventoryIp: "Add IP to Inventory",
    openUnifi: "Open in UniFi", lastRefresh: "Last refresh", sharedWith: "Also assigned to", ipUpdated: "Inventory IP updated",
    confirmIpUpdate: "Update the Inventory IP", missingIp: "No Inventory IP", niimbot: "NIIMBOT label printer",
    niimbotHelp: "Use the NIIMBOT printer configured in Home Assistant to print device labels.", selectPrinter: "Select printer",
    printerReady: "Printer ready", printerMissing: "NIIMBOT is not configured in Home Assistant", printLabel: "Print label",
    confirmPrint: "Print a label for this device?", printed: "Label sent to printer", labelWidth: "Label length (mm)",
    labelHeight: "Label width (mm)", labelMargin: "Side margin (mm)", labelTopMargin: "Top margin (mm)",
    network: "Network", vlan: "VLAN", ssid: "SSID", connectedDevice: "AP / switch", switchPort: "Switch port",
    tags: "Tags", allTags: "All tags", tagSettings: "Custom tags (one per line)", networkDetails: "Network details",
    backups: "Backup & restore", exportJson: "Export JSON", restoreJson: "Restore JSON", automaticBackups: "Automatic backups",
    restore: "Restore", confirmRestore: "Restore this backup? Current data will be backed up first.", restored: "Backup restored",
    logAction: "Action", logDevice: "Device", logChange: "Changes", logTime: "Date / time", logSource: "Source",
    noLogs: "No changes have been recorded yet.", backupBeforeImport: "An automatic backup was created before the import.",
    selected: "selected", selectAll: "Select all filtered", bulkEdit: "Bulk edit", clearSelection: "Clear selection",
    applyField: "Change", tagOperation: "Tag operation", keepTags: "Do not change tags", addTags: "Add tags",
    removeTags: "Remove tags", replaceTags: "Replace tags", bulkUpdated: "devices updated", bulkHelp: "Only checked fields will be changed.",
    fieldOptions: "Dropdown fields", fieldOptionsHelp: "Manage the available device types, brands, and tags.", configureIntegration: "Configure integration",
    createdAt: "Created", updatedAt: "Last updated", columns: "Columns", density: "Density", compactDensity: "Compact",
    normalDensity: "Normal", comfortableDensity: "Comfortable", savedViews: "Saved views", saveView: "Save view",
    deleteView: "Delete view", viewName: "View name", results: "results", pin: "Pin", show: "Show", resetColumns: "Reset columns",
    parentDevice: "Parent device", childDevice: "Child device", mainDevice: "Main device", copied: "Copied",
    batteryPowered: "Battery-powered", batteryLevel: "Battery", batteryEntity: "Battery entity", noBatteryEntity: "No battery entity",
    lastBatteryChange: "Last battery change", recordReplacement: "Record replacement", batteryHistory: "Battery history",
    replacementDate: "Replacement date", replacementNote: "Note", batteryDevices: "Battery devices", lowBattery: "Low battery",
    unavailable: "Unavailable", healthy: "Healthy", attention: "Attention", batteryOverview: "Battery overview",
    batteryHelp: "Devices with a Battery tag or an assigned battery entity.", replacementSaved: "Battery replacement recorded",
    noBatteryDevices: "No battery-powered devices found.", never: "Never", noBatteryData: "No live data",
    haPrimaryEntity: "HA Primary entity", selectPrimaryEntity: "Search and select the main Home Assistant entity",
    relatedBattery: "Same device", general: "General", generalSettings: "Regional formatting",
    generalSettingsHelp: "Choose how dates and times are displayed throughout Network Inventory.",
    timeFormat: "Time format", dateFormat: "Date format", twentyFourHour: "24-hour", twelveHour: "12-hour",
    dayFirst: "Day first", monthFirst: "Month first", formatPreview: "Preview"
  },
  el: {
    title: "Καταγραφή Συσκευών", overview: "Επισκόπηση", devices: "Συσκευές", newestDevices: "Νεότερες συσκευές", discover: "Discover", homeAssistant: "Home Assistant",
    settings: "Ρυθμίσεις", integrations: "Integrations", logs: "Logs", addDevice: "Νέα συσκευή", total: "Σύνολο συσκευών", areas: "Χώροι", brands: "Κατασκευαστές",
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
    apiKeyPlaceholder: "Επικόλληση του UniFi API key", unifiBadge: "Πληροφορίες σύνδεσης UniFi",
    allIpIssues: "Όλοι οι έλεγχοι IP", ipMismatch: "Διαφορά Inventory / UniFi", duplicateIp: "Διπλότυπη IP",
    unifiIp: "IP στο UniFi", inventoryIp: "IP στο Inventory", updateInventoryIp: "Ενημέρωση IP στο Inventory", addInventoryIp: "Προσθήκη IP στο Inventory",
    openUnifi: "Άνοιγμα στο UniFi", lastRefresh: "Τελευταία ανανέωση", sharedWith: "Χρησιμοποιείται επίσης από", ipUpdated: "Η IP στο Inventory ενημερώθηκε",
    confirmIpUpdate: "Να ενημερωθεί η IP στο Inventory", missingIp: "Χωρίς IP στο Inventory", niimbot: "Εκτυπωτής ετικετών NIIMBOT",
    niimbotHelp: "Χρησιμοποίησε τον NIIMBOT που έχει ρυθμιστεί στο Home Assistant για εκτύπωση ετικετών συσκευών.", selectPrinter: "Επιλογή εκτυπωτή",
    printerReady: "Ο εκτυπωτής είναι έτοιμος", printerMissing: "Το NIIMBOT δεν έχει ρυθμιστεί στο Home Assistant", printLabel: "Εκτύπωση label",
    confirmPrint: "Να εκτυπωθεί label για αυτή τη συσκευή;", printed: "Το label στάλθηκε στον εκτυπωτή", labelWidth: "Μήκος label (mm)",
    labelHeight: "Πλάτος label (mm)", labelMargin: "Πλευρικό περιθώριο (mm)", labelTopMargin: "Επάνω περιθώριο (mm)",
    network: "Δίκτυο", vlan: "VLAN", ssid: "SSID", connectedDevice: "AP / switch", switchPort: "Θύρα switch",
    tags: "Tags", allTags: "Όλα τα tags", tagSettings: "Custom tags (ένα ανά γραμμή)", networkDetails: "Στοιχεία δικτύου",
    backups: "Backup & επαναφορά", exportJson: "Εξαγωγή JSON", restoreJson: "Επαναφορά JSON", automaticBackups: "Αυτόματα backups",
    restore: "Επαναφορά", confirmRestore: "Να γίνει επαναφορά αυτού του backup; Θα αποθηκευτεί πρώτα η τωρινή κατάσταση.", restored: "Το backup επαναφέρθηκε",
    logAction: "Ενέργεια", logDevice: "Συσκευή", logChange: "Αλλαγές", logTime: "Ημερομηνία / ώρα", logSource: "Πηγή",
    noLogs: "Δεν έχουν καταγραφεί αλλαγές ακόμη.", backupBeforeImport: "Δημιουργήθηκε αυτόματο backup πριν από την εισαγωγή.",
    selected: "επιλεγμένες", selectAll: "Επιλογή όλων των φιλτραρισμένων", bulkEdit: "Μαζική επεξεργασία", clearSelection: "Καθαρισμός επιλογής",
    applyField: "Αλλαγή", tagOperation: "Ενέργεια tags", keepTags: "Να μην αλλάξουν τα tags", addTags: "Προσθήκη tags",
    removeTags: "Αφαίρεση tags", replaceTags: "Αντικατάσταση tags", bulkUpdated: "συσκευές ενημερώθηκαν", bulkHelp: "Θα αλλάξουν μόνο τα επιλεγμένα πεδία.",
    fieldOptions: "Πεδία dropdown", fieldOptionsHelp: "Διαχείριση διαθέσιμων τύπων συσκευής, brands και tags.", configureIntegration: "Ρύθμιση integration",
    createdAt: "Δημιουργήθηκε", updatedAt: "Τελευταία ενημέρωση", columns: "Στήλες", density: "Πυκνότητα", compactDensity: "Συμπαγής",
    normalDensity: "Κανονική", comfortableDensity: "Άνετη", savedViews: "Αποθηκευμένες προβολές", saveView: "Αποθήκευση προβολής",
    deleteView: "Διαγραφή προβολής", viewName: "Όνομα προβολής", results: "αποτελέσματα", pin: "Καρφίτσωμα", show: "Εμφάνιση", resetColumns: "Επαναφορά στηλών",
    parentDevice: "Γονική συσκευή", childDevice: "Child device", mainDevice: "Κύρια συσκευή", copied: "Αντιγράφηκε",
    batteryPowered: "Με μπαταρία", batteryLevel: "Μπαταρία", batteryEntity: "Entity μπαταρίας", noBatteryEntity: "Χωρίς entity μπαταρίας",
    lastBatteryChange: "Τελευταία αλλαγή μπαταρίας", recordReplacement: "Καταγραφή αλλαγής", batteryHistory: "Ιστορικό μπαταρίας",
    replacementDate: "Ημερομηνία αλλαγής", replacementNote: "Σημείωση", batteryDevices: "Συσκευές με μπαταρία", lowBattery: "Χαμηλή μπαταρία",
    unavailable: "Μη διαθέσιμη", healthy: "Καλή κατάσταση", attention: "Χρειάζεται προσοχή", batteryOverview: "Επισκόπηση μπαταριών",
    batteryHelp: "Συσκευές με tag Battery ή συνδεδεμένο entity μπαταρίας.", replacementSaved: "Η αλλαγή μπαταρίας καταγράφηκε",
    noBatteryDevices: "Δεν βρέθηκαν συσκευές που λειτουργούν με μπαταρία.", never: "Ποτέ", noBatteryData: "Χωρίς live δεδομένα",
    haPrimaryEntity: "HA Primary entity", selectPrimaryEntity: "Αναζήτησε και επίλεξε το κύριο entity του Home Assistant",
    relatedBattery: "Ίδια συσκευή", general: "Γενικά", generalSettings: "Μορφή ημερομηνίας και ώρας",
    generalSettingsHelp: "Επίλεξε πώς θα εμφανίζονται οι ημερομηνίες και οι ώρες σε όλο το Network Inventory.",
    timeFormat: "Μορφή ώρας", dateFormat: "Μορφή ημερομηνίας", twentyFourHour: "24ωρη", twelveHour: "12ωρη",
    dayFirst: "Πρώτα η ημέρα", monthFirst: "Πρώτα ο μήνας", formatPreview: "Παράδειγμα"
  }
};

const COLUMN_WIDTHS_KEY = "network-inventory-column-widths";
const TABLE_PREFERENCES_KEY = "network-inventory-table-preferences";
const DEFAULT_COLUMN_WIDTHS = {
  device_code: 90, name: 230, status: 100, device_type: 145, brand: 145, model: 155,
  area: 135, protocol: 125, mac: 175, ip_address: 135, battery_level: 135, network: 150, vlan: 90,
  ssid: 155, connected_device: 175, switch_port: 110, tags: 185
};
const DEFAULT_COLUMN_ORDER = Object.keys(DEFAULT_COLUMN_WIDTHS);
const FILTER_URL_KEYS = {
  query: "ni_q", protocolFilter: "ni_protocol", typeFilter: "ni_type", brandFilter: "ni_brand",
  areaFilter: "ni_area", statusFilter: "ni_status", ipFilter: "ni_ip", tagFilter: "ni_tag",
  sortKey: "ni_sort", sortDirection: "ni_direction"
};

function loadColumnWidths() {
  const stored = JSON.parse(localStorage.getItem(COLUMN_WIDTHS_KEY) || "{}");
  return { ...DEFAULT_COLUMN_WIDTHS, ...stored };
}

function loadTablePreferences() {
  const stored = JSON.parse(localStorage.getItem(TABLE_PREFERENCES_KEY) || "{}");
  const order = Array.isArray(stored.columnOrder) ? stored.columnOrder.filter(key => DEFAULT_COLUMN_ORDER.includes(key)) : [];
  const visible = Array.isArray(stored.visibleColumns) ? stored.visibleColumns.filter(key => DEFAULT_COLUMN_ORDER.includes(key)) : DEFAULT_COLUMN_ORDER;
  const pinned = Array.isArray(stored.pinnedColumns) ? stored.pinnedColumns.filter(key => DEFAULT_COLUMN_ORDER.includes(key)) : ["device_code", "name"];
  return {
    columnOrder: [...order, ...DEFAULT_COLUMN_ORDER.filter(key => !order.includes(key))],
    visibleColumns: visible.length ? visible : DEFAULT_COLUMN_ORDER,
    pinnedColumns: pinned,
    density: ["compact", "normal", "comfortable"].includes(stored.density) ? stored.density : "compact",
    savedViews: Array.isArray(stored.savedViews) ? stored.savedViews : []
  };
}

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
    this.ipFilter = "";
    this.tagFilter = "";
    this.selectedDevices = new Set();
    this.activeDeviceId = null;
    this.columnWidths = loadColumnWidths();
    const tablePreferences = loadTablePreferences();
    this.columnOrder = tablePreferences.columnOrder;
    this.visibleColumns = new Set(tablePreferences.visibleColumns);
    this.pinnedColumns = new Set(tablePreferences.pinnedColumns);
    this.tableDensity = tablePreferences.density;
    this.savedViews = tablePreferences.savedViews;
    this.activeSavedView = "";
    this.sortKey = "device_code";
    this.sortDirection = "asc";
    this.discoverView = "ha";
    this.settingsView = "general";
    this.loadFiltersFromUrl();
    this._started = false;
  }

  set hass(value) {
    this._hass = value;
    this.lang = value?.language?.startsWith("el") ? "el" : "en";
    if (this.data) {
      let batteryChanged = false;
      const updateLevel = item => {
        const state = value.states?.[item.entity_id || item.battery_entity_id];
        const level = batteryLevelFromState(state);
        const available = Boolean(state && !["unknown", "unavailable"].includes(state.state));
        if (item.level !== undefined) {
          if (item.level !== level || item.available !== available) batteryChanged = true;
          item.level = level;
          item.available = available;
        } else {
          if (item.battery_level !== level || item.battery_available !== available) batteryChanged = true;
          item.battery_level = level;
          item.battery_available = available;
        }
      };
      this.data.battery_entities?.forEach(updateLevel);
      this.data.devices.filter(device => device.battery_entity_id).forEach(updateLevel);
      if (batteryChanged && !this.shadowRoot.querySelector(".modal-backdrop")) this.render();
    }
    if (this.isConnected && !this._started) this.load();
  }

  set panel(value) { this._panel = value; }

  connectedCallback() {
    window.addEventListener("keydown", this.handleGlobalKeydown);
    if (!this._started && this._hass) this.load();
    else if (!this._started) this.renderLoading();
  }

  disconnectedCallback() { window.removeEventListener("keydown", this.handleGlobalKeydown); }

  handleGlobalKeydown = event => {
    if (event.key === "Escape" && this.activeDeviceId && !this.shadowRoot.querySelector(".modal-backdrop")) this.closeDeviceDrawer();
  };

  t(key) { return TEXT[this.lang || "en"][key] || TEXT.en[key] || key; }

  loadFiltersFromUrl() {
    const params = new URLSearchParams(window.location.search);
    Object.entries(FILTER_URL_KEYS).forEach(([property, parameter]) => {
      if (params.has(parameter)) this[property] = params.get(parameter) || "";
    });
    if (!DEFAULT_COLUMN_ORDER.includes(this.sortKey)) this.sortKey = "device_code";
    if (!['asc', 'desc'].includes(this.sortDirection)) this.sortDirection = "asc";
  }

  syncFiltersToUrl() {
    const url = new URL(window.location.href);
    Object.entries(FILTER_URL_KEYS).forEach(([property, parameter]) => {
      const value = this[property];
      const isDefaultSort = (property === "sortKey" && value === "device_code") || (property === "sortDirection" && value === "asc");
      if (value && !isDefaultSort) url.searchParams.set(parameter, value); else url.searchParams.delete(parameter);
    });
    window.history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
  }

  saveTablePreferences() {
    localStorage.setItem(TABLE_PREFERENCES_KEY, JSON.stringify({
      columnOrder: this.columnOrder,
      visibleColumns: [...this.visibleColumns],
      pinnedColumns: [...this.pinnedColumns],
      density: this.tableDensity,
      savedViews: this.savedViews
    }));
  }

  currentViewState() {
    return {
      filters: Object.fromEntries(Object.keys(FILTER_URL_KEYS).filter(key => !["sortKey", "sortDirection"].includes(key)).map(key => [key, this[key]])),
      sortKey: this.sortKey,
      sortDirection: this.sortDirection,
      columnOrder: [...this.columnOrder],
      visibleColumns: [...this.visibleColumns],
      pinnedColumns: [...this.pinnedColumns],
      density: this.tableDensity
    };
  }

  applySavedView(id) {
    this.activeSavedView = id;
    const view = this.savedViews.find(item => item.id === id);
    if (!view) return this.render();
    Object.assign(this, view.state.filters || {});
    this.sortKey = DEFAULT_COLUMN_ORDER.includes(view.state.sortKey) ? view.state.sortKey : "device_code";
    this.sortDirection = view.state.sortDirection === "desc" ? "desc" : "asc";
    this.columnOrder = [...(view.state.columnOrder || DEFAULT_COLUMN_ORDER)].filter(key => DEFAULT_COLUMN_ORDER.includes(key));
    this.columnOrder.push(...DEFAULT_COLUMN_ORDER.filter(key => !this.columnOrder.includes(key)));
    this.visibleColumns = new Set((view.state.visibleColumns || DEFAULT_COLUMN_ORDER).filter(key => DEFAULT_COLUMN_ORDER.includes(key)));
    this.pinnedColumns = new Set((view.state.pinnedColumns || []).filter(key => DEFAULT_COLUMN_ORDER.includes(key)));
    this.tableDensity = ["compact", "normal", "comfortable"].includes(view.state.density) ? view.state.density : "compact";
    this.syncFiltersToUrl();
    this.saveTablePreferences();
    this.render();
  }

  saveCurrentView() {
    const active = this.savedViews.find(item => item.id === this.activeSavedView);
    const name = prompt(this.t("viewName"), active?.name || "")?.trim();
    if (!name) return;
    const view = { id: active?.id || `view-${Date.now().toString(36)}`, name, state: this.currentViewState() };
    if (active) Object.assign(active, view); else this.savedViews.push(view);
    this.activeSavedView = view.id;
    this.saveTablePreferences();
    this.render();
  }

  deleteCurrentView() {
    if (!this.activeSavedView) return;
    this.savedViews = this.savedViews.filter(item => item.id !== this.activeSavedView);
    this.activeSavedView = "";
    this.saveTablePreferences();
    this.render();
  }

  resetColumns() {
    this.columnOrder = [...DEFAULT_COLUMN_ORDER];
    this.visibleColumns = new Set(DEFAULT_COLUMN_ORDER);
    this.pinnedColumns = new Set(["device_code", "name"]);
    this.tableDensity = "compact";
    this.activeSavedView = "";
    this.saveTablePreferences();
    this.render();
  }

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
      : this.view === "batteries" ? this.renderBatteries()
      : this.view === "discover" ? this.renderDiscover()
      : this.view === "integrations" ? this.renderIntegrations()
      : this.view === "logs" ? this.renderLogs()
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
          ${this.nav("batteries", "mdi:battery-medium", "batteryPowered", this.batteryDevices().length)}
          ${this.nav("discover", "mdi:radar", "discover", this.data.ha_devices.length + (this.data.unifi_items?.filter(item => !item.inventory_id).length || 0))}
          ${this.nav("integrations", "mdi:connection", "integrations")}
          ${this.nav("logs", "mdi:history", "logs", this.data.logs?.length || null)}
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

  subnav(group, value, label, icon, count = null) {
    const active = this[`${group}View`] === value;
    return `<button class="subnav ${active ? "active" : ""}" data-subnav-group="${group}" data-subnav-value="${value}"><ha-icon icon="${icon}"></ha-icon>${this.t(label)}${count !== null ? `<b>${count}</b>` : ""}</button>`;
  }

  renderOverview() {
    const devices = this.data.devices;
    const unique = key => new Set(devices.map(d => d[key]).filter(Boolean)).size;
    const groups = Object.entries(this.data.protocols).map(([key, p]) => ({
      key, ...p, count: devices.filter(d => d.protocol === key).length
    })).filter(item => item.count);
    let chartCursor = 0;
    const chartSegments = groups.map(group => {
      const start = chartCursor;
      chartCursor += devices.length ? group.count / devices.length * 100 : 0;
      return `${safeColor(group.color)} ${start}% ${chartCursor}%`;
    }).join(", ");
    const recent = [...devices].sort((a, b) => String(b.created_at || "").localeCompare(String(a.created_at || ""))).slice(0, 6);
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
          ${groups.length ? `<div class="protocol-chart-wrap"><div class="protocol-chart" style="background:conic-gradient(${chartSegments})"><span><strong>${devices.length}</strong><small>${this.t("devices")}</small></span></div></div>` : ""}
        </article>
        <article class="card"><h2>${this.t("newestDevices")}</h2>${this.deviceMiniList(recent)}</article>
      </section>`;
  }

  stat(icon, label, value, color) {
    return `<article class="stat"><div class="stat-icon ${color}"><ha-icon icon="${icon}"></ha-icon></div><div><span>${label}</span><strong>${value}</strong></div></article>`;
  }

  deviceMiniList(devices) {
    if (!devices.length) return `<p class="muted">${this.t("empty")}</p>`;
    return `<div class="mini-list">${devices.map(d => `<button data-edit="${d.id}"><span class="code">${d.device_code}</span><span><strong>${esc(d.name)}</strong><small>${esc(d.area || d.brand || this.t("manual"))}</small></span><ha-icon icon="mdi:chevron-right"></ha-icon></button>`).join("")}</div>`;
  }

  batteryDevices() {
    return this.data.devices.filter(device =>
      Boolean(device.battery_entity_id) || (device.tags || []).some(tag => tag.toLowerCase() === "battery")
    );
  }

  renderBatteries() {
    const devices = this.batteryDevices().sort((a, b) => {
      const first = a.battery_level ?? 101;
      const second = b.battery_level ?? 101;
      return first - second || a.name.localeCompare(b.name);
    });
    const low = devices.filter(device => device.battery_level !== null && device.battery_level <= 20).length;
    const unavailable = devices.filter(device => device.battery_entity_id && !device.battery_available).length;
    const withoutEntity = devices.filter(device => !device.battery_entity_id).length;
    const activeDevice = this.data.devices.find(device => device.id === this.activeDeviceId);
    return `<section class="section-head"><div><h2>${this.t("batteryOverview")}</h2><p>${this.t("batteryHelp")}</p></div></section>
      <section class="stats battery-stats">
        ${this.stat("mdi:battery", this.t("batteryDevices"), devices.length, "green")}
        ${this.stat("mdi:battery-alert", this.t("lowBattery"), low, "orange")}
        ${this.stat("mdi:battery-unknown", this.t("unavailable"), unavailable, "purple")}
        ${this.stat("mdi:link-off", this.t("noBatteryEntity"), withoutEntity, "blue")}
      </section>
      <section class="battery-grid">${devices.map(device => this.batteryCard(device)).join("")}</section>
      ${devices.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:battery-off-outline"></ha-icon><p>${this.t("noBatteryDevices")}</p></div>`}
      <button class="drawer-scrim ${activeDevice ? "open" : ""}" data-close-drawer aria-label="${this.t("cancel")}"></button>
      <aside id="device-drawer" class="device-drawer ${activeDevice ? "open" : ""}">${activeDevice ? this.renderDeviceDrawer(activeDevice) : ""}</aside>`;
  }

  batteryCard(device) {
    const level = device.battery_level;
    const tone = level === null ? "unknown" : level <= 20 ? "low" : level <= 40 ? "medium" : "good";
    return `<article class="battery-card card" data-device-row="${esc(device.id)}" tabindex="0">
      <div class="battery-card-head"><div><span class="code">#${esc(device.device_code)}</span><h3>${esc(device.name)}</h3><p>${esc([device.area, device.device_type].filter(Boolean).join(" · "))}</p></div>${this.batteryIndicator(device, true)}</div>
      <div class="battery-card-details"><div><span>${this.t("batteryEntity")}</span><strong class="mono">${esc(device.battery_entity_id || this.t("noBatteryEntity"))}</strong></div><div><span>${this.t("lastBatteryChange")}</span><strong>${esc(device.battery_last_replaced_at ? this.formatDateOnly(device.battery_last_replaced_at) : this.t("never"))}</strong></div></div>
      <div class="battery-card-actions"><span class="battery-health ${tone}">${this.t(tone === "good" ? "healthy" : tone === "unknown" ? "noBatteryData" : "attention")}</span><button class="secondary compact" data-battery-replace="${esc(device.id)}"><ha-icon icon="mdi:battery-sync-outline"></ha-icon>${this.t("recordReplacement")}</button></div>
    </article>`;
  }

  renderDevices() {
    const protocolOptions = Object.entries(this.data.protocols).map(([key, p]) => `<option value="${esc(key)}" ${this.protocolFilter === key ? "selected" : ""}>${esc(p.label)}</option>`).join("");
    const option = (value, selected) => `<option value="${esc(value)}" ${selected === value ? "selected" : ""}>${esc(value)}</option>`;
    const typeOptions = this.data.device_types.map(value => option(value, this.typeFilter)).join("");
    const brandOptions = this.data.brands.map(value => option(value, this.brandFilter)).join("");
    const areas = [...new Set([...this.data.areas, ...this.data.devices.map(device => device.area).filter(Boolean)])].sort((a,b) => a.localeCompare(b));
    const areaOptions = areas.map(value => option(value, this.areaFilter)).join("");
    const tagOptions = (this.data.tags || []).map(value => option(value, this.tagFilter)).join("");
    const devices = this.filteredDevices();
    const selectedCount = this.selectedDevices.size;
    const allFilteredSelected = devices.length && devices.every(device => this.selectedDevices.has(device.id));
    const activeDevice = this.data.devices.find(device => device.id === this.activeDeviceId);
    const columns = this.deviceColumns();
    const tableWidth = 44 + columns.reduce((total, column) => total + this.columnWidths[column.key], 0);
    const savedViewOptions = this.savedViews.map(view => `<option value="${esc(view.id)}" ${this.activeSavedView === view.id ? "selected" : ""}>${esc(view.name)}</option>`).join("");
    return `
      <section class="toolbar card">
        <label class="search"><ha-icon icon="mdi:magnify"></ha-icon><input id="search" value="${esc(this.query)}" placeholder="${this.t("search")}"></label>
        <select id="saved-view"><option value="">${this.t("savedViews")}</option>${savedViewOptions}</select>
        <button class="secondary icon-button" data-action="save-view" title="${this.t("saveView")}"><ha-icon icon="mdi:content-save-outline"></ha-icon></button>
        <button class="secondary icon-button" data-action="delete-view" title="${this.t("deleteView")}" ${this.activeSavedView ? "" : "disabled"}><ha-icon icon="mdi:bookmark-remove-outline"></ha-icon></button>
        <details class="columns-menu"><summary class="secondary"><ha-icon icon="mdi:view-column-outline"></ha-icon>${this.t("columns")}</summary><div class="columns-popover">
          <div class="column-list">${this.renderColumnSettings()}</div>
          <div class="density-setting"><span>${this.t("density")}</span>${["compact", "normal", "comfortable"].map(value => `<button class="${this.tableDensity === value ? "active" : ""}" data-density="${value}">${this.t(`${value}Density`)}</button>`).join("")}</div>
          <button class="secondary compact reset-columns" data-action="reset-columns"><ha-icon icon="mdi:restore"></ha-icon>${this.t("resetColumns")}</button>
        </div></details>
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
        <select id="ip-filter"><option value="">${this.t("allIpIssues")}</option><option value="mismatch" ${this.ipFilter === "mismatch" ? "selected" : ""}>${this.t("ipMismatch")}</option><option value="duplicate" ${this.ipFilter === "duplicate" ? "selected" : ""}>${this.t("duplicateIp")}</option></select>
        <select id="tag-filter"><option value="">${this.t("allTags")}</option>${tagOptions}</select>
        <button class="secondary" data-action="clear-filters"><ha-icon icon="mdi:filter-off-outline"></ha-icon>${this.t("clearFilters")}</button>
      </section>
      <section class="bulk-toolbar card ${selectedCount ? "active" : ""}"><label><input id="select-all-devices" type="checkbox" ${allFilteredSelected ? "checked" : ""}>${this.t("selectAll")}</label><span id="result-count">${devices.length} ${this.t("results")}</span><span id="selected-count">${selectedCount} ${this.t("selected")}</span><div><button class="secondary compact" data-action="clear-selection" ${selectedCount ? "" : "disabled"}>${this.t("clearSelection")}</button><button class="primary compact" data-action="bulk-edit" ${selectedCount ? "" : "disabled"}><ha-icon icon="mdi:pencil-multiple-outline"></ha-icon>${this.t("bulkEdit")}</button></div></section>
      <section class="table-card">
        <div class="table-scroll"><table class="device-table density-${this.tableDensity}" style="width:${tableWidth}px"><colgroup><col style="width:44px">${columns.map(column => `<col data-column-col="${column.key}" style="width:${this.columnWidths[column.key]}px">`).join("")}</colgroup><thead><tr>
          <th class="select-head"><input id="select-all-table" type="checkbox" ${allFilteredSelected ? "checked" : ""} aria-label="${this.t("selectAll")}"></th>
          ${columns.map(column => `<th data-column="${column.key}" class="${column.pinned ? "pinned-column" : ""}" style="${column.pinned ? `left:${column.left}px` : ""}"><button data-sort-column="${column.key}">${column.label}<ha-icon icon="${this.sortKey === column.key ? (this.sortDirection === "asc" ? "mdi:arrow-up" : "mdi:arrow-down") : "mdi:unfold-more-horizontal"}"></ha-icon></button><span class="column-resizer" data-resize-column="${column.key}"></span></th>`).join("")}
        </tr></thead><tbody>${devices.map(d => this.deviceRow(d, columns)).join("")}</tbody></table></div>
        <div id="devices-empty" class="empty" ${devices.length ? "hidden" : ""}><ha-icon icon="mdi:devices-off"></ha-icon><p>${this.t("empty")}</p></div>
      </section>
      <button class="drawer-scrim ${activeDevice ? "open" : ""}" data-close-drawer aria-label="${this.t("cancel")}"></button>
      <aside id="device-drawer" class="device-drawer ${activeDevice ? "open" : ""}">${activeDevice ? this.renderDeviceDrawer(activeDevice) : ""}</aside>`;
  }

  deviceColumns() {
    const definitions = this.allDeviceColumns();
    const ordered = this.columnOrder.map(key => definitions.find(column => column.key === key)).filter(Boolean);
    const visible = ordered.filter(column => this.visibleColumns.has(column.key));
    const columns = [...visible.filter(column => this.pinnedColumns.has(column.key)), ...visible.filter(column => !this.pinnedColumns.has(column.key))];
    let left = 44;
    return columns.map(column => {
      const pinned = this.pinnedColumns.has(column.key);
      const result = { ...column, pinned, left };
      if (pinned) left += this.columnWidths[column.key];
      return result;
    });
  }

  allDeviceColumns() {
    return [
      { key: "device_code", label: this.t("code") }, { key: "name", label: this.t("name") },
      { key: "status", label: this.t("status") }, { key: "device_type", label: this.t("type") },
      { key: "brand", label: this.t("brand") }, { key: "model", label: this.t("model") },
      { key: "area", label: this.t("area") }, { key: "protocol", label: this.t("protocol") },
      { key: "mac", label: this.t("address") }, { key: "ip_address", label: this.t("ip") },
      { key: "battery_level", label: this.t("batteryLevel") },
      { key: "network", label: this.t("network") }, { key: "vlan", label: this.t("vlan") },
      { key: "ssid", label: this.t("ssid") }, { key: "connected_device", label: this.t("connectedDevice") },
      { key: "switch_port", label: this.t("switchPort") }, { key: "tags", label: this.t("tags") }
    ];
  }

  renderColumnSettings() {
    const definitions = this.allDeviceColumns();
    return this.columnOrder.map(key => {
      const column = definitions.find(item => item.key === key);
      return `<div class="column-option" draggable="true" data-column-option="${key}"><ha-icon class="drag-handle" icon="mdi:drag"></ha-icon><label><input type="checkbox" data-column-visible="${key}" ${this.visibleColumns.has(key) ? "checked" : ""}>${column.label}</label><button class="pin-column ${this.pinnedColumns.has(key) ? "active" : ""}" data-pin-column="${key}" title="${this.t("pin")}"><ha-icon icon="mdi:pin-outline"></ha-icon></button></div>`;
    }).join("");
  }

  deviceRow(d, columns = this.deviceColumns()) {
    return `<tr class="device-row ${this.activeDeviceId === d.id ? "active" : ""}" data-device-row="${esc(d.id)}" tabindex="0">
      <td class="select-cell"><input type="checkbox" data-select-device="${esc(d.id)}" ${this.selectedDevices.has(d.id) ? "checked" : ""} aria-label="${this.t("selected")}"></td>
      ${columns.map(column => `<td data-column-cell="${column.key}" class="${column.pinned ? "pinned-column" : ""} ${["device_code", "mac", "ip_address"].includes(column.key) ? "mono" : ""}" style="${column.pinned ? `left:${column.left}px` : ""}">${this.deviceCell(d, column.key)}</td>`).join("")}
    </tr>`;
  }

  deviceCell(device, key) {
    const value = device[key];
    if (key === "device_code") return `<span class="code">${esc(value)}</span><button class="copy-cell" data-copy="${esc(value)}"><ha-icon icon="mdi:content-copy"></ha-icon></button>`;
    if (key === "name") return `<span class="device-name-cell"><strong>${esc(device.name)}</strong>${device.ha_device_kind === "child" ? `<ha-icon class="child-device-icon" icon="mdi:file-tree-outline" title="${this.t("childDevice")}"></ha-icon>` : ""}${this.data.unifi_matches?.[device.id] ? `<span class="unifi-dot" title="${this.t("unifiBadge")}"></span>` : ""}</span>`;
    if (key === "status") return this.statusBadge(device.status);
    if (key === "protocol") {
      const protocol = this.data.protocols[device.protocol] || { label: device.protocol, color: "#64748b" };
      return `<span class="pill" style="--pill:${safeColor(protocol.color)}">${esc(protocol.label)}</span>`;
    }
    if (key === "mac" || key === "ip_address") return `<span>${esc(value || "—")}</span>${value ? `<button class="copy-cell" data-copy="${esc(value)}"><ha-icon icon="mdi:content-copy"></ha-icon></button>` : ""}`;
    if (key === "battery_level") return device.battery_entity_id || (device.tags || []).some(tag => tag.toLowerCase() === "battery") ? this.batteryIndicator(device) : "—";
    if (key === "tags") return this.tagChips(device.tags);
    return esc(value || "—");
  }

  batteryIndicator(device, large = false) {
    const level = device.battery_level;
    if (level === null || level === undefined) return `<span class="battery-indicator unknown ${large ? "large" : ""}" title="${this.t("noBatteryData")}"><ha-icon icon="mdi:battery-unknown"></ha-icon><b>—</b></span>`;
    const tone = level <= 20 ? "low" : level <= 40 ? "medium" : "good";
    const icon = level <= 10 ? "mdi:battery-10" : level <= 20 ? "mdi:battery-20" : level <= 40 ? "mdi:battery-40" : level <= 60 ? "mdi:battery-60" : level <= 80 ? "mdi:battery-80" : "mdi:battery";
    return `<span class="battery-indicator ${tone} ${large ? "large" : ""}"><ha-icon icon="${icon}"></ha-icon><b>${esc(level)}%</b></span>`;
  }

  statusBadge(status) {
    const value = status || "unknown";
    return `<span class="device-status ${esc(value)}"><i></i>${esc(value === "unknown" ? this.t("unknown") : value)}</span>`;
  }

  renderDeviceDrawer(device) {
    const unifi = this.data.unifi_matches?.[device.id];
    const protocol = this.data.protocols[device.protocol] || { label: device.protocol, color: "#64748b" };
    const mismatch = this.hasIpMismatch(device);
    const duplicates = this.devicesWithIp(device.ip_address).filter(item => item.id !== device.id);
    const batteryPowered = Boolean(device.battery_entity_id) || (device.tags || []).some(tag => tag.toLowerCase() === "battery");
    const batteryHistory = [...(device.battery_history || [])].reverse();
    const row = (label, value, mono = false) => `<div><span>${label}</span><strong class="${mono ? "mono" : ""}">${esc(value || "—")}</strong></div>`;
    return `<div class="drawer-head"><div><span class="code">#${esc(device.device_code)}</span><h2>${esc(device.name)}</h2><div class="drawer-badges">${this.statusBadge(device.status)}<span class="pill" style="--pill:${safeColor(protocol.color)}">${esc(protocol.label)}</span>${unifi ? `<span class="unifi-badge"><ha-icon icon="mdi:access-point-network"></ha-icon>UniFi</span>` : ""}</div></div><button data-close-drawer title="${this.t("cancel")}"><ha-icon icon="mdi:close"></ha-icon></button></div>
      <div class="drawer-body">
        <section><h3>${this.t("details")}</h3>${row(this.t("type"), device.device_type)}${row(this.t("brand"), device.brand)}${row(this.t("model"), device.model)}${row(this.t("area"), device.area)}${device.ha_device_kind ? row(this.t("homeAssistant"), this.t(device.ha_device_kind === "child" ? "childDevice" : "mainDevice")) : ""}${device.parent_device_name ? row(this.t("parentDevice"), device.parent_device_name) : ""}${this.tagChips(device.tags)}</section>
        <section><h3>${this.t("networkDetails")}</h3>${row(this.t("address"), device.mac, true)}${row(this.t("ip"), device.ip_address, true)}${row(this.t("network"), device.network)}${row(this.t("vlan"), device.vlan)}${row(this.t("ssid"), device.ssid)}${row(this.t("connectedDevice"), device.connected_device)}${row(this.t("switchPort"), device.switch_port)}${mismatch ? `<button class="drawer-inline-action" data-sync-ip="${esc(device.id)}"><ha-icon icon="mdi:sync"></ha-icon>${this.t(device.ip_address ? "updateInventoryIp" : "addInventoryIp")} · ${esc(unifi.ip_address)}</button>` : ""}${duplicates.length ? `<p class="drawer-warning"><ha-icon icon="mdi:alert-circle-outline"></ha-icon>${this.t("sharedWith")}: ${esc(duplicates.map(item => `#${item.device_code} ${item.name}`).join(", "))}</p>` : ""}</section>
        ${batteryPowered ? `<section class="drawer-battery"><div class="drawer-section-title"><h3>${this.t("batteryPowered")}</h3>${this.batteryIndicator(device, true)}</div>${row(this.t("batteryEntity"), device.battery_entity_id || this.t("noBatteryEntity"), true)}${row(this.t("lastBatteryChange"), device.battery_last_replaced_at ? this.formatDateOnly(device.battery_last_replaced_at) : this.t("never"))}<button class="drawer-inline-action battery-action" data-battery-replace="${esc(device.id)}"><ha-icon icon="mdi:battery-sync-outline"></ha-icon>${this.t("recordReplacement")}</button>${batteryHistory.length ? `<div class="battery-history"><h4>${this.t("batteryHistory")}</h4>${batteryHistory.map(item => `<div><i></i><span><strong>${esc(this.formatDateOnly(item.replaced_at))}</strong>${item.note ? `<small>${esc(item.note)}</small>` : ""}</span></div>`).join("")}</div>` : ""}</section>` : ""}
        ${unifi ? `<section><h3>UniFi</h3>${row(this.t("type"), unifi.connection_type)}${row(this.t("firmware"), unifi.firmware_version)}${row(this.t("uplink"), [unifi.uplink_name, unifi.uplink_model, unifi.uplink_ip].filter(Boolean).join(" · "))}${row(this.t("connectedSince"), this.formatDate(unifi.connected_at))}${row(this.t("lastRefresh"), this.formatDate(this.data.integrations?.unifi?.last_refreshed))}</section>` : ""}
        <section><h3>${this.t("identifier")}</h3>${row(this.t("identifier"), device.device_identifier, true)}${row(this.t("haPrimaryEntity"), device.primary_entity_id, true)}${row(this.t("integration"), device.integration)}${device.ha_config_entry_id ? row("Config entry", device.ha_config_entry_id, true) : ""}${device.ha_config_subentry_id ? row("Config subentry", device.ha_config_subentry_id, true) : ""}${row(this.t("comments"), device.comments)}${row(this.t("createdAt"), this.formatDate(device.created_at))}${row(this.t("updatedAt"), this.formatDate(device.updated_at))}</section>
      </div>
      <div class="drawer-actions">${unifi ? `<a class="secondary drawer-icon-action" href="https://unifi.ui.com" target="_blank" rel="noopener noreferrer" title="${this.t("openUnifi")}"><ha-icon icon="mdi:open-in-new"></ha-icon></a>` : ""}${this.data.integrations?.niimbot?.connected ? `<button class="secondary" data-print-label="${esc(device.id)}"><ha-icon icon="mdi:printer-outline"></ha-icon>${this.t("printLabel")}</button>` : ""}<button class="primary" data-edit="${esc(device.id)}"><ha-icon icon="mdi:pencil-outline"></ha-icon>${this.t("edit")}</button><button class="secondary danger-text drawer-icon-action" data-delete="${esc(device.id)}" title="${this.t("delete")}"><ha-icon icon="mdi:delete-outline"></ha-icon></button></div>`;
  }

  tagChips(tags = []) {
    const visible = tags.slice(0, 3);
    return tags.length ? `<div class="tag-list">${visible.map(tag => `<span>${esc(tag)}</span>`).join("")}${tags.length > 3 ? `<span title="${esc(tags.slice(3).join(", "))}">+${tags.length - 3}</span>` : ""}</div>` : "";
  }

  renderDiscover() {
    const unifi = this.data.integrations?.unifi || {};
    const content = this.discoverView === "unifi"
      ? unifi.connected
        ? this.renderUnifi()
        : `<div class="empty standalone discover-empty"><ha-icon icon="mdi:access-point-network-off"></ha-icon><p>${this.t("notConnected")}</p><button class="primary" data-go-view="integrations">${this.t("configureIntegration")}</button></div>`
      : this.renderHaDevices();
    return `<div class="subnav-bar">${this.subnav("discover", "ha", "homeAssistant", "mdi:home-assistant", this.data.ha_devices.length)}${this.subnav("discover", "unifi", "unifi", "mdi:access-point-network", unifi.connected ? this.data.unifi_items.length : 0)}</div>${content}`;
  }

  renderHaDevices() {
    const devices = this.data.ha_devices;
    return `<section class="section-head"><div><h2>${this.t("homeAssistant")}</h2><p>${this.t("importHa")}</p></div></section>
      <section class="import-grid">${devices.map((d, index) => {
        const p = this.data.protocols[d.protocol] || this.data.protocols.other;
        return `<article class="import-card"><div class="device-icon"><ha-icon icon="${d.ha_device_kind === "child" ? "mdi:file-tree-outline" : "mdi:devices"}"></ha-icon></div><div class="grow"><h3>${esc(d.name)}</h3><p>${esc([d.brand, d.model].filter(Boolean).join(" · "))}</p><div class="meta"><span>${esc(d.area || "—")}</span><span>${esc(d.integration || "—")}</span><span>${this.t(d.ha_device_kind === "child" ? "childDevice" : "mainDevice")}${d.parent_device_name ? ` · ${esc(d.parent_device_name)}` : ""}</span><span class="pill" style="--pill:${safeColor(p.color)}">${esc(p.label)}</span></div></div><button class="primary compact" data-import="${index}">${this.t("import")}</button></article>`;
      }).join("")}</section>${devices.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:check-circle-outline"></ha-icon><p>${this.t("noHa")}</p></div>`}`;
  }

  renderIntegrations() {
    const state = this.data.integrations?.unifi || {};
    const niimbot = this.data.integrations?.niimbot || {};
    const options = (state.available_sites || []).map(site => `<option value="${esc(`${site.host_id}|${site.site_id}`)}">${esc(site.name)} · ${esc(site.gateway_mac || site.site_id)}</option>`).join("");
    const printerOptions = (niimbot.printers || []).map(printer => `<option value="${esc(printer.device_id)}" ${niimbot.device_id === printer.device_id ? "selected" : ""}>${esc(printer.name)}${printer.model ? ` · ${esc(printer.model)}` : ""}</option>`).join("");
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
      </article>
      <article class="card integration-card integration-gap">
        <div class="integration-logo niimbot-logo"><ha-icon icon="mdi:printer-outline"></ha-icon></div>
        <div class="grow"><div class="integration-title"><h2>${this.t("niimbot")}</h2><span class="status-dot ${niimbot.connected ? "ok" : ""}">${niimbot.connected ? this.t("printerReady") : this.t("notConnected")}</span></div>
          <p class="muted">${niimbot.installed ? this.t("niimbotHelp") : this.t("printerMissing")}</p>
          ${niimbot.installed && printerOptions ? `<form id="niimbot-form" class="inline-form niimbot-form"><label>${this.t("selectPrinter")}<select name="device_id" required><option value=""></option>${printerOptions}</select></label><label>${this.t("labelWidth")}<input name="label_width_mm" type="number" min="20" max="200" step="0.5" value="${esc(niimbot.label_width_mm || 30)}" required></label><label>${this.t("labelHeight")}<input name="label_height_mm" type="number" min="8" max="15" step="0.5" value="${esc(niimbot.label_height_mm || 15)}" required></label><label>${this.t("labelMargin")}<input name="margin_mm" type="number" min="0.5" max="3" step="0.5" value="${esc(niimbot.margin_mm || 1.5)}" required></label><label>${this.t("labelTopMargin")}<input name="top_margin_mm" type="number" min="0.5" max="4" step="0.5" value="${esc(niimbot.top_margin_mm || 2)}" required></label><button class="primary" type="submit">${this.t("save")}</button></form>` : ""}
        </div>
      </article>`;
  }

  renderUnifi() {
    const items = this.data.unifi_items || [];
    const state = this.data.integrations?.unifi || {};
    return `<section class="section-head"><div><h2>${this.t("unifi")}</h2><p>${this.t("activeClients")} · ${esc(state.site_name || "")}${state.last_refreshed ? ` · ${this.t("lastRefresh")}: ${esc(this.formatDate(state.last_refreshed))}` : ""}</p></div><button class="secondary" data-action="unifi-refresh"><ha-icon icon="mdi:refresh"></ha-icon>${this.t("refresh")}</button></section>
      <section class="import-grid">${items.map((item, index) => {
        const p = this.data.protocols[item.protocol] || this.data.protocols.other;
        const inventory = item.inventory_id ? this.data.devices.find(device => device.id === item.inventory_id) : null;
        const mismatch = inventory && this.hasIpMismatch(inventory);
        return `<article class="import-card"><div class="device-icon unifi-icon"><ha-icon icon="${item.kind === "infrastructure" ? "mdi:access-point-network" : item.protocol === "wifi" ? "mdi:wifi" : "mdi:ethernet"}"></ha-icon></div><div class="grow"><h3>${esc(item.name)}</h3><p>${esc([item.ip_address, item.mac].filter(Boolean).join(" · "))}</p>${mismatch ? `<p class="ip-warning">${this.t("inventoryIp")}: ${esc(inventory.ip_address || "—")}</p>` : ""}<div class="meta"><span>${esc(item.connection_type || "—")}</span>${item.uplink_name ? `<span>${this.t("uplink")}: ${esc(item.uplink_name)}</span>` : ""}<span class="pill" style="--pill:${safeColor(p.color)}">${esc(p.label)}</span></div></div><div class="card-actions"><a class="secondary compact" href="https://unifi.ui.com" target="_blank" rel="noopener noreferrer"><ha-icon icon="mdi:open-in-new"></ha-icon>${this.t("openUnifi")}</a>${mismatch ? `<button class="secondary compact" data-sync-ip="${esc(item.inventory_id)}"><ha-icon icon="mdi:sync"></ha-icon>${this.t(inventory.ip_address ? "updateInventoryIp" : "addInventoryIp")}</button>` : ""}${item.inventory_id ? `<button class="secondary compact" data-unifi-details-inventory="${esc(item.inventory_id)}"><ha-icon icon="mdi:check"></ha-icon>${this.t("added")}</button>` : `<button class="primary compact" data-unifi-import="${index}">${this.t("import")}</button>`}</div></article>`;
      }).join("")}</section>${items.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:lan-disconnect"></ha-icon><p>${this.t("noUnifi")}</p></div>`}`;
  }

  renderLogs() {
    const logs = [...(this.data.logs || [])].reverse();
    const actionLabel = action => ({ add: this.t("addDevice"), update: this.t("edit"), bulk_update: this.t("bulkEdit"), battery_replaced: this.t("recordReplacement"), delete: this.t("delete"), import: this.t("import"), restore: this.t("restore"), settings: this.t("settings") }[action] || action);
    return `<section class="section-head"><div><h2>${this.t("logs")}</h2><p>${logs.length} ${this.t("logAction").toLowerCase()}</p></div></section>
      <section class="log-list">${logs.map(log => `<article class="card log-entry"><div class="log-icon ${esc(log.action)}"><ha-icon icon="${log.action === "delete" ? "mdi:delete-outline" : log.action === "restore" ? "mdi:backup-restore" : "mdi:pencil-outline"}"></ha-icon></div><div class="grow"><div class="log-title"><strong>${esc(actionLabel(log.action))}</strong>${log.device_name ? `<span>#${esc(log.device_code)} · ${esc(log.device_name)}</span>` : ""}</div><small>${esc(this.formatDate(log.timestamp))} · ${esc(log.source || "manual")}</small>${log.details ? `<p>${esc(log.details)}</p>` : ""}<div class="change-list">${(log.changes || []).map(change => `<div><b>${esc(this.fieldLabel(change.field))}</b><span>${esc(displayValue(change.old))}</span><ha-icon icon="mdi:arrow-right"></ha-icon><span>${esc(displayValue(change.new))}</span></div>`).join("")}</div></div></article>`).join("")}</section>
      ${logs.length ? "" : `<div class="empty standalone"><ha-icon icon="mdi:history"></ha-icon><p>${this.t("noLogs")}</p></div>`}`;
  }

  fieldLabel(fieldName) {
    const labels = { name:"name", device_type:"type", brand:"brand", model:"model", area:"area", mac:"address", ip_address:"ip", protocol:"protocol", device_identifier:"identifier", primary_entity_id:"haPrimaryEntity", comments:"comments", status:"status", battery_entity_id:"batteryEntity", battery_last_replaced_at:"lastBatteryChange", battery_history:"batteryHistory", network:"network", vlan:"vlan", ssid:"ssid", connected_device:"connectedDevice", switch_port:"switchPort", tags:"tags" };
    return this.t(labels[fieldName] || fieldName);
  }

  renderSettings() {
    const tabs = `<div class="subnav-bar">${this.subnav("settings", "general", "general", "mdi:tune-variant")}${this.subnav("settings", "fields", "fieldOptions", "mdi:form-dropdown")}${this.subnav("settings", "ranges", "ranges", "mdi:numeric")}${this.subnav("settings", "backups", "backups", "mdi:backup-restore")}</div>`;
    const content = this.settingsView === "general" ? this.renderGeneralSettings()
      : this.settingsView === "ranges" ? this.renderRangeSettings()
      : this.settingsView === "backups" ? this.renderBackupSettings()
      : this.renderFieldSettings();
    return tabs + content;
  }

  renderGeneralSettings() {
    const general = this.data.general || { time_format: "24h", date_format: "day_first" };
    const sample = new Date(2026, 8, 22, 17, 45);
    return `<form id="settings-form"><section class="section-head"><div><h2>${this.t("generalSettings")}</h2><p>${this.t("generalSettingsHelp")}</p></div></section>
      <section class="card settings-card general-settings">
        <label><span><strong>${this.t("timeFormat")}</strong><small>${general.time_format === "12h" ? "5:45 PM" : "17:45"}</small></span><select id="time-format"><option value="24h" ${general.time_format === "24h" ? "selected" : ""}>${this.t("twentyFourHour")} · 17:45</option><option value="12h" ${general.time_format === "12h" ? "selected" : ""}>${this.t("twelveHour")} · 5:45 PM</option></select></label>
        <label><span><strong>${this.t("dateFormat")}</strong><small>${general.date_format === "month_first" ? "09/22/2026" : "22/09/2026"}</small></span><select id="date-format"><option value="day_first" ${general.date_format === "day_first" ? "selected" : ""}>${this.t("dayFirst")} · DD/MM/YYYY</option><option value="month_first" ${general.date_format === "month_first" ? "selected" : ""}>${this.t("monthFirst")} · MM/DD/YYYY</option></select></label>
        <div class="format-preview"><ha-icon icon="mdi:calendar-clock-outline"></ha-icon><span><small>${this.t("formatPreview")}</small><strong id="format-preview-value">${esc(formatDateWithPreferences(sample, general, true))}</strong></span></div>
      </section>
      <div class="form-actions"><button type="submit" class="primary"><ha-icon icon="mdi:content-save-outline"></ha-icon>${this.t("saveSettings")}</button></div>
    </form>`;
  }

  renderFieldSettings() {
    return `<form id="settings-form"><section class="section-head"><div><h2>${this.t("fieldOptions")}</h2><p>${this.t("fieldOptionsHelp")}</p></div></section>
      <section class="card settings-card"><h2>${this.t("deviceTypes")}</h2><textarea id="device-types" rows="12">${esc(this.data.device_types.join("\n"))}</textarea></section>
      <section class="card settings-card"><h2>${this.t("brandSettings")}</h2><textarea id="brands" rows="8">${esc(this.data.brands.join("\n"))}</textarea></section>
      <section class="card settings-card"><h2>${this.t("tagSettings")}</h2><textarea id="tags" rows="8">${esc((this.data.tags || []).join("\n"))}</textarea></section>
      <div class="form-actions"><button type="submit" class="primary"><ha-icon icon="mdi:content-save-outline"></ha-icon>${this.t("saveSettings")}</button></div>
    </form>`;
  }

  renderRangeSettings() {
    const rows = Object.entries(this.data.protocols).map(([key, p]) => this.protocolRow(key, p)).join("");
    return `<form id="settings-form">
      <section class="card settings-card"><div class="section-head"><div><h2>${this.t("ranges")}</h2><p>${this.t("rangeHelp")}</p></div><button type="button" class="secondary" data-action="add-protocol"><ha-icon icon="mdi:plus"></ha-icon>${this.t("addProtocol")}</button></div>
        <div id="protocol-rows" class="protocol-settings">${rows}</div>
      </section>
      <div class="form-actions"><button type="submit" class="primary"><ha-icon icon="mdi:content-save-outline"></ha-icon>${this.t("saveSettings")}</button></div>
    </form>`;
  }

  renderBackupSettings() {
    return `<section class="card settings-card backup-card"><div class="section-head"><div><h2>${this.t("backups")}</h2><p>${this.t("automaticBackups")}</p></div><div class="backup-actions"><input id="json-file" type="file" accept="application/json,.json" hidden><button class="secondary" data-action="restore-json"><ha-icon icon="mdi:backup-restore"></ha-icon>${this.t("restoreJson")}</button><button class="secondary" data-action="export-json"><ha-icon icon="mdi:download"></ha-icon>${this.t("exportJson")}</button></div></div>
      <div class="backup-list">${(this.data.backups || []).map(backup => `<div><span><strong>${esc(this.formatDate(backup.created_at))}</strong><small>${esc(backup.reason)} · ${esc(backup.device_count)} ${this.t("devices").toLowerCase()}</small></span><button class="secondary compact" data-restore-backup="${esc(backup.id)}">${this.t("restore")}</button></div>`).join("") || `<p class="muted">${this.t("automaticBackups")}: 0</p>`}</div>
    </section>`;
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
      this.activeDeviceId = null;
      this.view = button.dataset.view; this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-subnav-group]").forEach(button => button.addEventListener("click", () => {
      this[`${button.dataset.subnavGroup}View`] = button.dataset.subnavValue;
      this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-go-view]").forEach(button => button.addEventListener("click", () => {
      this.view = button.dataset.goView;
      this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-action='add']").forEach(button => button.addEventListener("click", () => this.openDeviceModal()));
    this.shadowRoot.querySelectorAll("[data-edit]").forEach(button => button.addEventListener("click", () => {
      if (button.closest("#device-drawer")) return;
      const device = this.data.devices.find(item => item.id === button.dataset.edit); if (device) this.openDeviceModal(device);
    }));
    this.shadowRoot.querySelectorAll("[data-delete]").forEach(button => button.addEventListener("click", () => {
      if (!button.closest("#device-drawer")) this.deleteDevice(button.dataset.delete);
    }));
    this.shadowRoot.querySelectorAll("[data-select-device]").forEach(input => input.addEventListener("change", () => {
      if (input.checked) this.selectedDevices.add(input.dataset.selectDevice); else this.selectedDevices.delete(input.dataset.selectDevice);
      this.updateSelectionUi();
    }));
    this.shadowRoot.querySelector("#select-all-devices")?.addEventListener("change", event => {
      this.filteredDevices().forEach(device => event.target.checked ? this.selectedDevices.add(device.id) : this.selectedDevices.delete(device.id));
      this.updateSelectionUi();
    });
    this.shadowRoot.querySelector("#select-all-table")?.addEventListener("change", event => {
      this.filteredDevices().forEach(device => event.target.checked ? this.selectedDevices.add(device.id) : this.selectedDevices.delete(device.id));
      this.updateSelectionUi();
    });
    this.shadowRoot.querySelector("[data-action='clear-selection']")?.addEventListener("click", () => { this.selectedDevices.clear(); this.updateSelectionUi(); });
    this.shadowRoot.querySelector("[data-action='bulk-edit']")?.addEventListener("click", () => this.openBulkEditModal());
    this.shadowRoot.querySelector("#search")?.addEventListener("input", event => {
      this.query = event.target.value;
      this.activeSavedView = "";
      this.syncFiltersToUrl();
      this.refreshDeviceBody();
    });
    [["protocol", "protocolFilter"], ["type", "typeFilter"], ["brand", "brandFilter"], ["area", "areaFilter"], ["status", "statusFilter"], ["ip", "ipFilter"], ["tag", "tagFilter"]].forEach(([id, property]) => {
      this.shadowRoot.querySelector(`#${id}-filter`)?.addEventListener("change", event => {
        this[property] = event.target.value;
        this.activeSavedView = "";
        this.syncFiltersToUrl();
        this.render();
      });
    });
    this.shadowRoot.querySelector("[data-action='clear-filters']")?.addEventListener("click", () => {
      this.protocolFilter = this.typeFilter = this.brandFilter = this.areaFilter = this.statusFilter = this.ipFilter = this.tagFilter = "";
      this.query = "";
      this.activeSavedView = "";
      this.syncFiltersToUrl();
      this.render();
    });
    this.shadowRoot.querySelector("#saved-view")?.addEventListener("change", event => this.applySavedView(event.target.value));
    this.shadowRoot.querySelector("[data-action='save-view']")?.addEventListener("click", () => this.saveCurrentView());
    this.shadowRoot.querySelector("[data-action='delete-view']")?.addEventListener("click", () => this.deleteCurrentView());
    this.shadowRoot.querySelector("[data-action='reset-columns']")?.addEventListener("click", () => this.resetColumns());
    this.shadowRoot.querySelectorAll("[data-sort-column]").forEach(button => button.addEventListener("click", () => {
      const key = button.dataset.sortColumn;
      this.sortDirection = this.sortKey === key && this.sortDirection === "asc" ? "desc" : "asc";
      this.sortKey = key;
      this.activeSavedView = "";
      this.syncFiltersToUrl();
      this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-column-visible]").forEach(input => input.addEventListener("change", () => {
      if (input.checked) this.visibleColumns.add(input.dataset.columnVisible); else this.visibleColumns.delete(input.dataset.columnVisible);
      if (!this.visibleColumns.size) {
        this.visibleColumns.add(input.dataset.columnVisible);
        input.checked = true;
        return;
      }
      this.activeSavedView = "";
      this.saveTablePreferences();
      this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-pin-column]").forEach(button => button.addEventListener("click", event => {
      event.preventDefault();
      const key = button.dataset.pinColumn;
      if (this.pinnedColumns.has(key)) this.pinnedColumns.delete(key); else this.pinnedColumns.add(key);
      this.activeSavedView = "";
      this.saveTablePreferences();
      this.render();
    }));
    this.shadowRoot.querySelectorAll("[data-density]").forEach(button => button.addEventListener("click", event => {
      event.preventDefault();
      this.tableDensity = button.dataset.density;
      this.activeSavedView = "";
      this.saveTablePreferences();
      this.render();
    }));
    this.bindColumnOrdering();
    this.shadowRoot.querySelector("[data-action='export']")?.addEventListener("click", () => this.exportCsv());
    this.shadowRoot.querySelector("[data-action='csv']")?.addEventListener("click", () => this.shadowRoot.querySelector("#csv-file").click());
    this.shadowRoot.querySelector("#csv-file")?.addEventListener("change", event => this.importCsv(event.target.files[0]));
    this.shadowRoot.querySelectorAll("[data-import]").forEach(button => button.addEventListener("click", () => this.openDeviceModal(this.data.ha_devices[Number(button.dataset.import)], true)));
    this.shadowRoot.querySelectorAll("[data-unifi-import]").forEach(button => button.addEventListener("click", () => this.openDeviceModal(this.unifiImportDevice(this.data.unifi_items[Number(button.dataset.unifiImport)]), true)));
    this.shadowRoot.querySelectorAll("[data-unifi-details]").forEach(button => button.addEventListener("click", () => this.openUnifiDetails(this.data.unifi_matches[button.dataset.unifiDetails])));
    this.shadowRoot.querySelectorAll("[data-unifi-details-inventory]").forEach(button => button.addEventListener("click", () => this.openUnifiDetails(this.data.unifi_matches[button.dataset.unifiDetailsInventory])));
    this.shadowRoot.querySelectorAll("[data-sync-ip]").forEach(button => button.addEventListener("click", () => {
      if (!button.closest("#device-drawer")) this.updateInventoryIp(button.dataset.syncIp);
    }));
    this.shadowRoot.querySelectorAll("[data-print-label]").forEach(button => button.addEventListener("click", () => {
      if (!button.closest("#device-drawer")) this.printLabel(button.dataset.printLabel, button);
    }));
    this.shadowRoot.querySelectorAll("[data-battery-replace]").forEach(button => button.addEventListener("click", event => {
      if (button.closest("#device-drawer")) return;
      event.stopPropagation();
      this.openBatteryReplacementModal(button.dataset.batteryReplace);
    }));
    this.shadowRoot.querySelector("#unifi-connect-form")?.addEventListener("submit", event => this.connectUnifi(event));
    this.shadowRoot.querySelector("#unifi-site-form")?.addEventListener("submit", event => this.selectUnifiSite(event));
    this.shadowRoot.querySelector("#niimbot-form")?.addEventListener("submit", event => this.configureNiimbot(event));
    this.shadowRoot.querySelectorAll("[data-action='unifi-refresh']").forEach(button => button.addEventListener("click", () => this.refreshUnifi(button)));
    this.shadowRoot.querySelectorAll("[data-action='unifi-disconnect']").forEach(button => button.addEventListener("click", () => this.disconnectUnifi(button)));
    this.shadowRoot.querySelector("[data-action='add-protocol']")?.addEventListener("click", () => this.addProtocolRow());
    this.shadowRoot.querySelectorAll("[data-remove-protocol]").forEach(button => button.addEventListener("click", () => button.closest(".protocol-setting").remove()));
    this.shadowRoot.querySelectorAll("#time-format,#date-format").forEach(select => select.addEventListener("change", () => this.updateFormatPreview()));
    this.shadowRoot.querySelector("#settings-form")?.addEventListener("submit", event => this.saveSettings(event));
    this.shadowRoot.querySelector("[data-action='export-json']")?.addEventListener("click", () => this.exportJson());
    this.shadowRoot.querySelector("[data-action='restore-json']")?.addEventListener("click", () => this.shadowRoot.querySelector("#json-file").click());
    this.shadowRoot.querySelector("#json-file")?.addEventListener("change", event => this.restoreJson(event.target.files[0]));
    this.shadowRoot.querySelectorAll("[data-restore-backup]").forEach(button => button.addEventListener("click", () => this.restoreInternalBackup(button.dataset.restoreBackup)));
    this.bindDeviceTableEvents();
    this.bindDeviceDrawerEvents();
    this.bindColumnResizers();
  }

  refreshDeviceBody() {
    const tbody = this.shadowRoot.querySelector("tbody");
    if (!tbody) return;
    const devices = this.filteredDevices();
    tbody.innerHTML = devices.map(d => this.deviceRow(d)).join("");
    const resultCount = this.shadowRoot.querySelector("#result-count");
    if (resultCount) resultCount.textContent = `${devices.length} ${this.t("results")}`;
    const empty = this.shadowRoot.querySelector("#devices-empty");
    if (empty) empty.hidden = Boolean(devices.length);
    tbody.querySelectorAll("[data-select-device]").forEach(input => input.addEventListener("change", () => {
      if (input.checked) this.selectedDevices.add(input.dataset.selectDevice); else this.selectedDevices.delete(input.dataset.selectDevice);
      this.updateSelectionUi();
    }));
    this.bindDeviceTableEvents(tbody);
  }

  bindDeviceTableEvents(root = this.shadowRoot) {
    root.querySelectorAll("[data-device-row]").forEach(row => {
      const open = event => {
        if (event.type === "keydown" && !["Enter", " "].includes(event.key)) return;
        if (event.target.closest("input,button,a")) return;
        event.preventDefault();
        this.openDeviceDrawer(row.dataset.deviceRow);
      };
      row.addEventListener("click", open);
      row.addEventListener("keydown", open);
    });
    this.bindCopyButtons(root);
  }

  bindCopyButtons(root = this.shadowRoot) {
    root.querySelectorAll("[data-copy]").forEach(button => button.addEventListener("click", async event => {
      event.stopPropagation();
      await navigator.clipboard.writeText(button.dataset.copy);
      this.toast(this.t("copied"));
    }));
  }

  bindColumnOrdering() {
    let draggedKey = "";
    this.shadowRoot.querySelectorAll("[data-column-option]").forEach(option => {
      option.addEventListener("dragstart", event => {
        draggedKey = option.dataset.columnOption;
        option.classList.add("dragging");
        event.dataTransfer.effectAllowed = "move";
      });
      option.addEventListener("dragend", () => option.classList.remove("dragging"));
      option.addEventListener("dragover", event => event.preventDefault());
      option.addEventListener("drop", event => {
        event.preventDefault();
        const targetKey = option.dataset.columnOption;
        if (!draggedKey || draggedKey === targetKey) return;
        const order = this.columnOrder.filter(key => key !== draggedKey);
        order.splice(order.indexOf(targetKey), 0, draggedKey);
        this.columnOrder = order;
        this.activeSavedView = "";
        this.saveTablePreferences();
        this.render();
      });
    });
  }

  updateSelectionUi() {
    const count = this.selectedDevices.size;
    const filtered = this.filteredDevices();
    const allSelected = Boolean(filtered.length) && filtered.every(device => this.selectedDevices.has(device.id));
    const toolbar = this.shadowRoot.querySelector(".bulk-toolbar");
    toolbar?.classList.toggle("active", Boolean(count));
    const label = this.shadowRoot.querySelector("#selected-count");
    if (label) label.textContent = `${count} ${this.t("selected")}`;
    this.shadowRoot.querySelectorAll("#select-all-devices,#select-all-table").forEach(input => input.checked = allSelected);
    this.shadowRoot.querySelectorAll("[data-select-device]").forEach(input => input.checked = this.selectedDevices.has(input.dataset.selectDevice));
    const clear = this.shadowRoot.querySelector("[data-action='clear-selection']");
    const bulk = this.shadowRoot.querySelector("[data-action='bulk-edit']");
    if (clear) clear.disabled = !count;
    if (bulk) bulk.disabled = !count;
  }

  openDeviceDrawer(deviceId) {
    const device = this.data.devices.find(item => item.id === deviceId);
    if (!device) return;
    this.activeDeviceId = deviceId;
    this.shadowRoot.querySelectorAll("[data-device-row]").forEach(row => row.classList.toggle("active", row.dataset.deviceRow === deviceId));
    const drawer = this.shadowRoot.querySelector("#device-drawer");
    drawer.innerHTML = this.renderDeviceDrawer(device);
    drawer.classList.add("open");
    this.shadowRoot.querySelector(".drawer-scrim")?.classList.add("open");
    this.bindDeviceDrawerEvents();
  }

  closeDeviceDrawer() {
    this.activeDeviceId = null;
    this.shadowRoot.querySelector("#device-drawer")?.classList.remove("open");
    this.shadowRoot.querySelector(".drawer-scrim")?.classList.remove("open");
    this.shadowRoot.querySelectorAll("[data-device-row]").forEach(row => row.classList.remove("active"));
  }

  bindDeviceDrawerEvents() {
    const drawer = this.shadowRoot.querySelector("#device-drawer");
    this.shadowRoot.querySelectorAll("[data-close-drawer]").forEach(button => button.onclick = () => this.closeDeviceDrawer());
    if (!drawer?.classList.contains("open")) return;
    drawer.querySelector("[data-edit]")?.addEventListener("click", event => {
      const device = this.data.devices.find(item => item.id === event.currentTarget.dataset.edit);
      if (device) this.openDeviceModal(device);
    });
    drawer.querySelector("[data-delete]")?.addEventListener("click", event => this.deleteDevice(event.currentTarget.dataset.delete));
    drawer.querySelector("[data-print-label]")?.addEventListener("click", event => this.printLabel(event.currentTarget.dataset.printLabel, event.currentTarget));
    drawer.querySelector("[data-sync-ip]")?.addEventListener("click", event => this.updateInventoryIp(event.currentTarget.dataset.syncIp));
    drawer.querySelector("[data-battery-replace]")?.addEventListener("click", event => this.openBatteryReplacementModal(event.currentTarget.dataset.batteryReplace));
  }

  bindColumnResizers() {
    this.shadowRoot.querySelectorAll("[data-resize-column]").forEach(handle => handle.addEventListener("pointerdown", event => {
      event.preventDefault();
      const key = handle.dataset.resizeColumn;
      const startX = event.clientX;
      const startWidth = this.columnWidths[key];
      const move = moveEvent => {
        this.columnWidths[key] = Math.max(72, startWidth + moveEvent.clientX - startX);
        const col = this.shadowRoot.querySelector(`[data-column-col='${key}']`);
        if (col) col.style.width = `${this.columnWidths[key]}px`;
        const table = this.shadowRoot.querySelector(".device-table");
        if (table) table.style.width = `${44 + this.deviceColumns().reduce((total, column) => total + this.columnWidths[column.key], 0)}px`;
      };
      const stop = () => {
        window.removeEventListener("pointermove", move);
        window.removeEventListener("pointerup", stop);
        localStorage.setItem(COLUMN_WIDTHS_KEY, JSON.stringify(this.columnWidths));
      };
      window.addEventListener("pointermove", move);
      window.addEventListener("pointerup", stop);
    }));
  }

  unifiImportDevice(item) {
    return {
      ...item,
      area: "",
      integration: "unifi",
      device_identifier: `unifi:${item.id}`,
      primary_entity_id: "",
      comments: item.uplink_name ? `${this.t("uplink")}: ${item.uplink_name}` : "",
      unifi_id: item.id,
      unifi_kind: item.kind,
      unifi_site_id: this.data.integrations?.unifi?.site_id || "",
      network: item.network || "",
      vlan: item.vlan || "",
      ssid: item.ssid || "",
      connected_device: item.connected_device || item.uplink_name || "",
      switch_port: item.switch_port || "",
      tags: []
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
      this.view = "discover";
      this.discoverView = "unifi";
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

  async configureNiimbot(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const device_id = String(new FormData(form).get("device_id") || "");
    const label_width_mm = Number(new FormData(form).get("label_width_mm"));
    const label_height_mm = Number(new FormData(form).get("label_height_mm"));
    const margin_mm = Number(new FormData(form).get("margin_mm"));
    const top_margin_mm = Number(new FormData(form).get("top_margin_mm"));
    if (!device_id) return;
    this.setBusy(form, true);
    try {
      await this._hass.callWS({ type: "network_inventory/niimbot/configure", device_id, label_width_mm, label_height_mm, margin_mm, top_margin_mm });
      await this.reload(this.t("saved"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  async printLabel(deviceId, button) {
    const device = this.data.devices.find(item => item.id === deviceId);
    if (!device || !confirm(`${this.t("confirmPrint")}\n${device.name} · ID ${device.device_code}`)) return;
    button.disabled = true;
    try {
      await this._hass.callWS({ type: "network_inventory/niimbot/print", device_id: deviceId });
      this.toast(this.t("printed"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
    finally { button.disabled = false; }
  }

  openUnifiDetails(item) {
    if (!item) return;
    const modal = this.shadowRoot.querySelector("#modal");
    const inventory = item.inventory_id ? this.data.devices.find(device => device.id === item.inventory_id) : null;
    const mismatch = inventory && this.hasIpMismatch(inventory);
    const refreshed = this.data.integrations?.unifi?.last_refreshed;
    const rows = [
      [this.t("name"), item.name], [this.t("address"), item.mac], [this.t("unifiIp"), item.ip_address],
      ...(inventory ? [[this.t("inventoryIp"), inventory.ip_address || "—"]] : []),
      [this.t("type"), item.connection_type], [this.t("model"), item.model], [this.t("firmware"), item.firmware_version],
      [this.t("network"), item.network], [this.t("vlan"), item.vlan], [this.t("ssid"), item.ssid], [this.t("switchPort"), item.switch_port],
      [this.t("uplink"), [item.uplink_name, item.uplink_model, item.uplink_ip].filter(Boolean).join(" · ")],
      [this.t("connectedSince"), this.formatDate(item.connected_at)], [this.t("lastRefresh"), this.formatDate(refreshed)]
    ].filter(([, value]) => value);
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal details-modal"><div class="modal-head"><div><h2>${esc(item.name)}</h2><p>UniFi · ${esc(item.connection_type || item.kind)}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div><div class="detail-list">${rows.map(([label, value]) => `<div><span>${esc(label)}</span><strong>${esc(value)}</strong></div>`).join("")}</div><div class="modal-actions"><a class="secondary" href="https://unifi.ui.com" target="_blank" rel="noopener noreferrer"><ha-icon icon="mdi:open-in-new"></ha-icon>${this.t("openUnifi")}</a>${mismatch ? `<button class="primary" data-sync-ip="${esc(inventory.id)}"><ha-icon icon="mdi:sync"></ha-icon>${this.t(inventory.ip_address ? "updateInventoryIp" : "addInventoryIp")}</button>` : ""}</div></section></div>`;
    modal.querySelector("[data-close]").addEventListener("click", () => modal.innerHTML = "");
    modal.querySelector("[data-sync-ip]")?.addEventListener("click", event => this.updateInventoryIp(event.currentTarget.dataset.syncIp));
  }

  normalizedIp(value) { return String(value || "").trim().toLowerCase(); }

  devicesWithIp(ip) {
    const normalized = this.normalizedIp(ip);
    return normalized ? this.data.devices.filter(device => this.normalizedIp(device.ip_address) === normalized) : [];
  }

  hasIpMismatch(device) {
    const unifi = this.data.unifi_matches?.[device.id];
    return Boolean(unifi?.ip_address && this.normalizedIp(unifi.ip_address) !== this.normalizedIp(device.ip_address));
  }

  async updateInventoryIp(deviceId) {
    const device = this.data.devices.find(item => item.id === deviceId);
    const unifi = this.data.unifi_matches?.[deviceId];
    if (!device || !unifi?.ip_address) return;
    const oldIp = device.ip_address || this.t("missingIp");
    if (!confirm(`${this.t("confirmIpUpdate")};\n${oldIp} → ${unifi.ip_address}`)) return;
    try {
      await this._hass.callWS({ type: "network_inventory/update", device_id: deviceId, device: { ip_address: unifi.ip_address } });
      this.shadowRoot.querySelector("#modal").innerHTML = "";
      await this.reload(this.t("ipUpdated"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  filteredDevices() {
    const q = this.query.toLowerCase();
    const devices = [...this.data.devices].filter(device =>
      (!this.protocolFilter || device.protocol === this.protocolFilter) &&
      (!this.typeFilter || device.device_type === this.typeFilter) &&
      (!this.brandFilter || device.brand === this.brandFilter) &&
      (!this.areaFilter || device.area === this.areaFilter) &&
      (!this.statusFilter || device.status === this.statusFilter) &&
      (!this.tagFilter || (device.tags || []).includes(this.tagFilter)) &&
      (!this.ipFilter || (this.ipFilter === "mismatch" && this.hasIpMismatch(device)) || (this.ipFilter === "duplicate" && this.devicesWithIp(device.ip_address).length > 1)) &&
      (!q || Object.values(device).join(" ").toLowerCase().includes(q))
    );
    const sortValue = device => this.sortKey === "tags" ? (device.tags || []).join(" ") : device[this.sortKey];
    return devices.sort((a, b) => {
      const first = sortValue(a);
      const second = sortValue(b);
      const comparison = typeof first === "number" && typeof second === "number"
        ? first - second
        : String(first || "").localeCompare(String(second || ""), undefined, { numeric: true, sensitivity: "base" });
      return (comparison || a.device_code - b.device_code) * (this.sortDirection === "desc" ? -1 : 1);
    });
  }

  openBatteryReplacementModal(deviceId) {
    const device = this.data.devices.find(item => item.id === deviceId);
    if (!device) return;
    const today = localDateValue(new Date());
    const modal = this.shadowRoot.querySelector("#modal");
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal battery-modal"><div class="modal-head"><div><h2>${this.t("recordReplacement")}</h2><p>#${esc(device.device_code)} · ${esc(device.name)}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div><form id="battery-replacement-form"><div class="form-grid"><label>${this.t("replacementDate")}<input name="replaced_at" type="date" max="${today}" value="${today}" required></label><label class="full">${this.t("replacementNote")}<textarea name="note" rows="3"></textarea></label></div><div class="modal-actions"><button type="button" class="secondary" data-close>${this.t("cancel")}</button><button type="submit" class="primary"><ha-icon icon="mdi:battery-sync-outline"></ha-icon>${this.t("recordReplacement")}</button></div></form></section></div>`;
    modal.querySelectorAll("[data-close]").forEach(button => button.addEventListener("click", () => modal.innerHTML = ""));
    modal.querySelector("#battery-replacement-form").addEventListener("submit", event => this.saveBatteryReplacement(event, deviceId));
  }

  async saveBatteryReplacement(event, deviceId) {
    event.preventDefault();
    const form = event.currentTarget;
    const values = Object.fromEntries(new FormData(form).entries());
    this.setBusy(form, true);
    try {
      await this._hass.callWS({ type: "network_inventory/battery_replaced", device_id: deviceId, replaced_at: values.replaced_at, note: values.note.trim() });
      this.shadowRoot.querySelector("#modal").innerHTML = "";
      await this.reload(this.t("replacementSaved"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  openBulkEditModal() {
    if (!this.selectedDevices.size) return;
    const selectOptions = values => values.map(value => `<option value="${esc(value)}">${esc(value)}</option>`).join("");
    const fieldRow = (name, label, control) => `<div class="bulk-field"><label class="apply-check"><input type="checkbox" name="apply_${name}" data-enable-field="${name}">${this.t("applyField")}</label><label>${label}${control}</label></div>`;
    const tagOptions = (this.data.tags || []).map(tag => `<label><input type="checkbox" name="bulk_tags" value="${esc(tag)}">${esc(tag)}</label>`).join("");
    const modal = this.shadowRoot.querySelector("#modal");
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal"><div class="modal-head"><div><h2>${this.t("bulkEdit")}</h2><p>${this.selectedDevices.size} ${this.t("selected")} · ${this.t("bulkHelp")}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div>
      <form id="bulk-edit-form"><div class="bulk-form">
        ${fieldRow("device_type", this.t("type"), `<select name="device_type" disabled><option value=""></option>${selectOptions(this.data.device_types)}</select>`)}
        ${fieldRow("brand", this.t("brand"), `<select name="brand" disabled><option value=""></option>${selectOptions(this.data.brands)}</select>`)}
        ${fieldRow("network", this.t("network"), `<input name="network" disabled>`)}
        ${fieldRow("vlan", this.t("vlan"), `<input name="vlan" disabled>`)}
        ${fieldRow("ssid", this.t("ssid"), `<input name="ssid" disabled>`)}
        ${fieldRow("connected_device", this.t("connectedDevice"), `<input name="connected_device" disabled>`)}
        ${fieldRow("switch_port", this.t("switchPort"), `<input name="switch_port" disabled>`)}
        <div class="bulk-tags"><label>${this.t("tagOperation")}<select name="tag_mode"><option value="">${this.t("keepTags")}</option><option value="add">${this.t("addTags")}</option><option value="remove">${this.t("removeTags")}</option><option value="replace">${this.t("replaceTags")}</option></select></label><div class="bulk-tag-options disabled">${tagOptions}</div></div>
      </div><div class="modal-actions"><button type="button" class="secondary" data-close>${this.t("cancel")}</button><button type="submit" class="primary">${this.t("save")}</button></div></form></section></div>`;
    modal.querySelectorAll("[data-close]").forEach(button => button.addEventListener("click", () => modal.innerHTML = ""));
    modal.querySelectorAll("[data-enable-field]").forEach(check => check.addEventListener("change", () => {
      const input = modal.querySelector(`[name='${check.dataset.enableField}']`);
      input.disabled = !check.checked;
      if (check.checked) input.focus();
    }));
    const tagMode = modal.querySelector("[name='tag_mode']");
    tagMode.addEventListener("change", () => {
      const enabled = Boolean(tagMode.value);
      modal.querySelector(".bulk-tag-options").classList.toggle("disabled", !enabled);
      modal.querySelectorAll("[name='bulk_tags']").forEach(input => input.disabled = !enabled);
    });
    modal.querySelectorAll("[name='bulk_tags']").forEach(input => input.disabled = true);
    modal.querySelector("#bulk-edit-form").addEventListener("submit", event => this.saveBulkEdit(event));
  }

  async saveBulkEdit(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const fields = {};
    ["device_type", "brand", "network", "vlan", "ssid", "connected_device", "switch_port"].forEach(name => {
      if (form.elements[`apply_${name}`].checked) fields[name] = form.elements[name].value.trim();
    });
    const tag_mode = form.elements.tag_mode.value;
    const tags = [...form.querySelectorAll("[name='bulk_tags']:checked")].map(input => input.value);
    this.setBusy(form, true);
    try {
      const result = await this._hass.callWS({ type: "network_inventory/bulk_update", device_ids: [...this.selectedDevices], fields, tag_mode, tags });
      this.selectedDevices.clear();
      this.shadowRoot.querySelector("#modal").innerHTML = "";
      await this.reload(`${result.updated} ${this.t("bulkUpdated")}`);
    } catch (error) { this.toast(error?.message || this.t("error"), true); this.setBusy(form, false); }
  }

  openDeviceModal(device = null, isImport = false) {
    const protocols = Object.entries(this.data.protocols).map(([key,p]) => `<option value="${esc(key)}" ${(device?.protocol || "wifi") === key ? "selected" : ""}>${esc(p.label)}</option>`).join("");
    const types = this.data.device_types.map(type => `<option value="${esc(type)}" ${device?.device_type === type ? "selected" : ""}>${esc(type)}</option>`).join("");
    const brands = [...this.data.brands];
    if (device?.brand && !brands.some(brand => brand.toLowerCase() === device.brand.toLowerCase())) brands.push(device.brand);
    const brandOptions = brands.sort((a,b) => a.localeCompare(b)).map(brand => `<option value="${esc(brand)}" ${device?.brand === brand ? "selected" : ""}>${esc(brand)}</option>`).join("");
    const areaOptions = this.data.areas.map(area => `<option value="${esc(area)}"></option>`).join("");
    const selectedTags = new Set(device?.tags || []);
    const tagOptions = (this.data.tags || []).map(tag => `<label><input type="checkbox" name="tags" value="${esc(tag)}" ${selectedTags.has(tag) ? "checked" : ""}>${esc(tag)}</label>`).join("");
    const isEdit = Boolean(device && !isImport);
    const isChildDevice = device?.ha_device_kind === "child";
    const ipRequired = !isChildDevice && ["wifi", "ethernet"].includes(device?.protocol || "wifi");
    const haEntities = this.data.ha_entities || [];
    const primaryEntityOptions = haEntities.map(entity => `<option value="${esc(entity.entity_id)}">${esc(entity.name)} · ${esc(entity.entity_id)}</option>`).join("");
    const selectedPrimary = haEntities.find(entity => entity.entity_id === device?.primary_entity_id);
    const relatedDeviceId = selectedPrimary?.device_id || device?.ha_device_id || "";
    const relatedBatteryEntities = (this.data.battery_entities || []).filter(entity => entity.device_id && entity.device_id === relatedDeviceId);
    const initialBatteryEntity = device?.battery_entity_id || (relatedBatteryEntities.length === 1 ? relatedBatteryEntities[0].entity_id : "");
    const batteryOptionsFor = (selected, relatedId) => {
      const batteryEntities = [...(this.data.battery_entities || [])].sort((a, b) => {
        const aRelated = a.device_id && a.device_id === relatedId ? 1 : 0;
        const bRelated = b.device_id && b.device_id === relatedId ? 1 : 0;
        return bRelated - aRelated || a.name.localeCompare(b.name);
      });
      const missing = selected && !batteryEntities.some(entity => entity.entity_id === selected)
        ? `<option value="${esc(selected)}" selected>${esc(selected)} · ${this.t("unavailable")}</option>`
        : "";
      return `<option value="">${this.t("noBatteryEntity")}</option>${missing}${batteryEntities.map(entity => `<option value="${esc(entity.entity_id)}" ${selected === entity.entity_id ? "selected" : ""}>${entity.device_id && entity.device_id === relatedId ? `★ ${this.t("relatedBattery")} · ` : ""}${esc(entity.name)} · ${esc(entity.entity_id)}${entity.level !== null ? ` · ${esc(entity.level)}%` : ""}</option>`).join("")}`;
    };
    const modal = this.shadowRoot.querySelector("#modal");
    modal.innerHTML = `<div class="modal-backdrop"><section class="modal"><div class="modal-head"><div><h2>${isEdit ? this.t("edit") : this.t("addDevice")}</h2><p>${isEdit ? `${this.t("code")}: ${device.device_code}` : this.t("autoId")}</p></div><button type="button" data-close><ha-icon icon="mdi:close"></ha-icon></button></div>
      <form id="device-form"><div class="form-grid">
        ${isEdit ? `<label>${this.t("code")}<div class="id-field"><input name="device_code" value="${esc(device.device_code)}" readonly><button type="button" class="secondary" data-clear-id title="${this.t("clearId")}"><ha-icon icon="mdi:close"></ha-icon></button></div><small data-id-help></small></label>` : ""}
        ${field("name", this.t("name"), device?.name, true)}
        <label>${this.t("type")}<select name="device_type" required><option value=""></option>${types}</select></label>
        <label>${this.t("brand")}<select name="brand" required><option value=""></option>${brandOptions}</select></label>${field("model", this.t("model"), device?.model)}
        <label>${this.t("area")}<input name="area" list="area-options" value="${esc(device?.area || "")}" required><datalist id="area-options">${areaOptions}</datalist></label>
        <label>${this.t("protocol")}<select name="protocol" required>${protocols}</select><small>${isEdit ? this.t("stableId") : ""}</small></label>
        ${field("mac", this.t("address"), device?.mac, !isChildDevice)}${field("ip_address", this.t("ip"), device?.ip_address, ipRequired)}
        ${field("device_identifier", this.t("identifier"), device?.device_identifier)}<label>${this.t("haPrimaryEntity")}<input name="primary_entity_id" list="ha-primary-entities" value="${esc(device?.primary_entity_id || "")}" placeholder="${this.t("selectPrimaryEntity")}"><datalist id="ha-primary-entities">${primaryEntityOptions}</datalist></label>
        ${field("integration", this.t("integration"), device?.integration)}
        <label>${this.t("status")}<select name="status"><option value="unknown">${this.t("unknown")}</option><option value="online" ${device?.status === "online" ? "selected" : ""}>Online</option><option value="offline" ${device?.status === "offline" ? "selected" : ""}>Offline</option></select></label>
        <fieldset class="full battery-fields"><legend>${this.t("batteryPowered")}</legend><label>${this.t("batteryEntity")}<select name="battery_entity_id">${batteryOptionsFor(initialBatteryEntity, relatedDeviceId)}</select></label><label>${this.t("lastBatteryChange")}<input name="battery_last_replaced_at" type="date" value="${esc(device?.battery_last_replaced_at || "")}"></label></fieldset>
        <fieldset class="full network-fields"><legend>${this.t("networkDetails")}</legend>${field("network", this.t("network"), device?.network)}${field("vlan", this.t("vlan"), device?.vlan)}${field("ssid", this.t("ssid"), device?.ssid)}${field("connected_device", this.t("connectedDevice"), device?.connected_device)}${field("switch_port", this.t("switchPort"), device?.switch_port)}</fieldset>
        <label class="full">${this.t("tags")}<details class="tag-picker"><summary>${selectedTags.size ? esc([...selectedTags].join(", ")) : this.t("tags")}</summary><div>${tagOptions || `<small>${this.t("tagSettings")}</small>`}</div></details></label>
        <label class="full">${this.t("comments")}<textarea name="comments" rows="3">${esc(device?.comments || "")}</textarea></label>
      </div><div class="modal-actions"><button type="button" class="secondary" data-close>${this.t("cancel")}</button><button type="submit" class="primary">${this.t("save")}</button></div></form></section></div>`;
    modal.querySelectorAll("[data-close]").forEach(button => button.addEventListener("click", () => modal.innerHTML = ""));
    const protocolSelect = modal.querySelector("[name='protocol']");
    const ipInput = modal.querySelector("[name='ip_address']");
    protocolSelect.addEventListener("change", () => { ipInput.required = !isChildDevice && ["wifi", "ethernet"].includes(protocolSelect.value); });
    const primaryInput = modal.querySelector("[name='primary_entity_id']");
    const batterySelect = modal.querySelector("[name='battery_entity_id']");
    primaryInput.addEventListener("change", () => {
      const primary = haEntities.find(entity => entity.entity_id === primaryInput.value.trim());
      const relatedId = primary?.device_id || "";
      const relatedBatteries = (this.data.battery_entities || []).filter(entity => entity.device_id && entity.device_id === relatedId);
      const automaticBattery = relatedBatteries.length === 1 ? relatedBatteries[0].entity_id : "";
      batterySelect.innerHTML = batteryOptionsFor(automaticBattery, relatedId);
      batterySelect.value = automaticBattery;
    });
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
    payload.tags = [...form.querySelectorAll("[name='tags']:checked")].map(input => input.value);
    const primaryEntity = (this.data.ha_entities || []).find(entity => entity.entity_id === payload.primary_entity_id);
    if (primaryEntity?.device_id) payload.ha_device_id = primaryEntity.device_id;
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
    try { await this._hass.callWS({ type: "network_inventory/delete", device_id: id }); this.selectedDevices.delete(id); await this.reload(this.t("saved")); }
    catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async importCsv(file) {
    if (!file) return;
    try {
      const rows = csvToDevices(await file.text());
      const result = await this._hass.callWS({ type: "network_inventory/import", devices: rows });
      await this.reload(`${result.imported} ${this.t("imported")}, ${result.skipped} ${this.t("skipped")}${result.backup_id ? ` · ${this.t("backupBeforeImport")}` : ""}`);
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  exportCsv() {
    const headers = ["Device Code","MAC / IEEE Address","Device IP","Device Type","Brand","Area","Device Name","Device ID","HA Primary Entity","Comments","Protocol","Network","VLAN","SSID","AP / Switch","Switch Port","Tags","Battery Entity","Last Battery Change"];
    const keys = ["device_code","mac","ip_address","device_type","brand","area","name","device_identifier","primary_entity_id","comments","protocol","network","vlan","ssid","connected_device","switch_port","tags","battery_entity_id","battery_last_replaced_at"];
    const lines = [headers, ...this.data.devices.sort((a,b) => a.device_code-b.device_code).map(d => keys.map(k => Array.isArray(d[k]) ? d[k].join(";") : (d[k] ?? "")))];
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
    const protocolRows = this.shadowRoot.querySelectorAll(".protocol-setting");
    const protocols = protocolRows.length ? {} : this.data.protocols;
    protocolRows.forEach(row => {
      const values = Object.fromEntries(new FormData(wrapForm(row)).entries());
      protocols[values.key] = { label: values.label, start: Number(values.start), end: Number(values.end), color: values.color };
    });
    const device_types = this.shadowRoot.querySelector("#device-types")?.value.split("\n").map(v => v.trim()).filter(Boolean) || this.data.device_types;
    const brands = this.shadowRoot.querySelector("#brands")?.value.split("\n").map(v => v.trim()).filter(Boolean) || this.data.brands;
    const tags = this.shadowRoot.querySelector("#tags")?.value.split("\n").map(v => v.trim()).filter(Boolean) || this.data.tags;
    const general = {
      time_format: this.shadowRoot.querySelector("#time-format")?.value || this.data.general.time_format,
      date_format: this.shadowRoot.querySelector("#date-format")?.value || this.data.general.date_format
    };
    try { await this._hass.callWS({ type: "network_inventory/settings", settings: { general, protocols, device_types, brands, tags } }); await this.reload(this.t("saved")); }
    catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  updateFormatPreview() {
    const preferences = {
      time_format: this.shadowRoot.querySelector("#time-format").value,
      date_format: this.shadowRoot.querySelector("#date-format").value
    };
    this.shadowRoot.querySelector("#format-preview-value").textContent = formatDateWithPreferences(new Date(2026, 8, 22, 17, 45), preferences, true);
  }

  async exportJson() {
    try {
      const backup = await this._hass.callWS({ type: "network_inventory/export" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(new Blob([JSON.stringify(backup, null, 2)], { type: "application/json" }));
      link.download = `network-inventory-backup-${new Date().toISOString().slice(0,10)}.json`;
      link.click(); URL.revokeObjectURL(link.href);
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async restoreJson(file) {
    if (!file || !confirm(this.t("confirmRestore"))) return;
    try {
      const backup = JSON.parse(await file.text());
      await this._hass.callWS({ type: "network_inventory/restore", backup });
      await this.reload(this.t("restored"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async restoreInternalBackup(backupId) {
    if (!confirm(this.t("confirmRestore"))) return;
    try {
      await this._hass.callWS({ type: "network_inventory/restore_backup", backup_id: backupId });
      await this.reload(this.t("restored"));
    } catch (error) { this.toast(error?.message || this.t("error"), true); }
  }

  async reload(message) {
    this.data = await this._hass.callWS({ type: "network_inventory/list" });
    const validIds = new Set(this.data.devices.map(device => device.id));
    this.selectedDevices = new Set([...this.selectedDevices].filter(id => validIds.has(id)));
    if (!validIds.has(this.activeDeviceId)) this.activeDeviceId = null;
    this.render(); this.toast(message);
  }

  toast(message, error = false) {
    const target = this.shadowRoot.querySelector("#toast");
    if (!target) return;
    target.textContent = message; target.className = error ? "show error" : "show";
    clearTimeout(this._toastTimer); this._toastTimer = setTimeout(() => target.className = "", 3200);
  }

  formatDate(value) { return formatDateWithPreferences(value, this.data.general, true); }

  formatDateOnly(value) {
    if (!value) return "";
    return formatDateWithPreferences(new Date(`${value}T00:00:00`), this.data.general, false);
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
function formatDateWithPreferences(value, preferences, includeTime) {
  if (!value) return "";
  const date = value instanceof Date ? value : new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  const locale = preferences?.date_format === "month_first" ? "en-US" : "en-GB";
  const options = { day: "2-digit", month: "2-digit", year: "numeric" };
  if (includeTime) Object.assign(options, { hour: "numeric", minute: "2-digit", hour12: preferences?.time_format === "12h" });
  return new Intl.DateTimeFormat(locale, options).format(date);
}
function localDateValue(date) { return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`; }
function batteryLevelFromState(state) { if (!state || ["unknown", "unavailable"].includes(state.state)) return null; const level = Number(state.state); return Number.isFinite(level) ? Math.max(0, Math.min(100, Math.round(level * 10) / 10)) : null; }
function displayValue(value) { if (Array.isArray(value)) return value.join(", ") || "—"; if (value && typeof value === "object") return JSON.stringify(value); return String(value ?? "") || "—"; }
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
    primary_entity_id: find("haprimaryentity", "primaryentity", "primaryentityid"),
    comments: find("comments", "notes"), protocol: find("protocol", "connection"),
    network: find("network", "networkname"), vlan: find("vlan", "vlanid"), ssid: find("ssid"),
    connected_device: find("apswitch", "connecteddevice", "uplink"), switch_port: find("switchport", "port"), tags: find("tags"),
    battery_entity_id: find("batteryentity", "batteryentityid"), battery_last_replaced_at: find("lastbatterychange", "batterylastreplacedat")
  };
  if (index.protocol < 0 && rows[0].length >= 10 && rows[0].length <= 11) index.protocol = rows[0].length - 1;
  return rows.slice(1).map(row => {
    const item = Object.fromEntries(Object.entries(index).map(([key, i]) => [key, i >= 0 ? (row[i] || "").trim() : ""]));
    item.tags = item.tags ? item.tags.split(";").map(tag => tag.trim()).filter(Boolean) : [];
    return item;
  }).filter(item => item.name);
}

const BASE_CSS = `
  .integration-gap{margin-top:14px}.niimbot-logo{background:#f3e8ff!important;color:#7e22ce!important}.niimbot-form{max-width:none;flex-wrap:wrap}.niimbot-form label:first-child{min-width:230px}.niimbot-form label:not(:first-child){max-width:145px}
  :host{display:block;min-height:100%;background:var(--primary-background-color);color:var(--primary-text-color);font-family:var(--paper-font-body1_-_font-family,system-ui,sans-serif)}
  *{box-sizing:border-box}button,input,select,textarea{font:inherit;color:inherit}button{cursor:pointer}.app{max-width:none;margin:auto;padding:24px 28px 60px}header{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:22px}h1{font-size:28px;margin:0 0 3px;letter-spacing:-.4px}h2{font-size:18px;margin:0 0 18px}h3{font-size:15px;margin:0 0 5px}p{margin:0}header p,.section-head p,.muted{color:var(--secondary-text-color);font-size:13px}
  .title-row{display:flex;align-items:center;gap:9px}.version{font-size:11px;font-weight:700;color:var(--secondary-text-color);border:1px solid var(--divider-color);border-radius:20px;padding:3px 7px}
  button{border:0;background:none}.primary,.secondary{height:42px;border-radius:10px;padding:0 15px;display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:650;white-space:nowrap}.primary{background:var(--primary-color);color:#fff}.secondary{border:1px solid var(--divider-color);background:var(--card-background-color)}.compact{height:36px;padding:0 12px;font-size:13px}button:disabled{opacity:.55;cursor:wait}
  nav{display:flex;gap:5px;border-bottom:1px solid var(--divider-color);margin-bottom:24px;overflow:auto}.nav{padding:12px 15px;display:flex;align-items:center;gap:8px;color:var(--secondary-text-color);border-bottom:2px solid transparent;white-space:nowrap}.nav.active{color:var(--primary-color);border-color:var(--primary-color);font-weight:650}.nav b{font-size:11px;background:var(--primary-color);color:#fff;border-radius:20px;padding:2px 6px}.subnav-bar{display:flex;gap:7px;margin-bottom:18px;padding:5px;background:var(--secondary-background-color);border-radius:12px;width:max-content;max-width:100%;overflow:auto}.subnav{height:38px;padding:0 13px;border-radius:8px;display:flex;align-items:center;gap:7px;white-space:nowrap;color:var(--secondary-text-color)}.subnav.active{background:var(--card-background-color);color:var(--primary-color);font-weight:650;box-shadow:0 1px 4px #0002}.subnav b{font-size:10px;background:var(--divider-color);border-radius:12px;padding:2px 6px}.subnav ha-icon{--mdc-icon-size:18px}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}.stat,.card,.table-card,.import-card{background:var(--card-background-color);border:1px solid var(--divider-color);border-radius:14px}.stat{padding:18px;display:flex;align-items:center;gap:14px}.stat-icon{width:44px;height:44px;border-radius:12px;display:grid;place-items:center}.stat-icon.blue{background:#dbeafe;color:#2563eb}.stat-icon.green{background:#d1fae5;color:#059669}.stat-icon.orange{background:#ffedd5;color:#ea580c}.stat-icon.purple{background:#ede9fe;color:#7c3aed}.stat span{display:block;font-size:12px;color:var(--secondary-text-color);margin-bottom:3px}.stat strong{font-size:24px}.grid-two{display:grid;grid-template-columns:1fr 1.3fr;gap:16px}.card{padding:20px}.protocol-list>div{display:grid;grid-template-columns:10px 90px 1fr 28px;align-items:center;gap:9px;margin:14px 0;font-size:13px}.dot{width:9px;height:9px;border-radius:50%}.bar{height:7px;background:var(--divider-color);border-radius:10px;overflow:hidden}.bar i{display:block;height:100%;border-radius:10px}.protocol-chart-wrap{display:grid;place-items:center;border-top:1px solid var(--divider-color);margin-top:18px;padding-top:20px}.protocol-chart{width:160px;height:160px;border-radius:50%;display:grid;place-items:center;position:relative}.protocol-chart:after{content:"";position:absolute;width:92px;height:92px;border-radius:50%;background:var(--card-background-color)}.protocol-chart span{z-index:1;text-align:center}.protocol-chart strong{display:block;font-size:25px}.protocol-chart small{display:block;color:var(--secondary-text-color);font-size:11px;margin-top:2px}.mini-list button{width:100%;display:grid;grid-template-columns:58px 1fr 24px;align-items:center;text-align:left;padding:10px 5px;border-bottom:1px solid var(--divider-color)}.mini-list button:last-child{border:0}.mini-list small,td small{display:block;color:var(--secondary-text-color);margin-top:3px}.code{font-family:ui-monospace,monospace;font-weight:750;color:var(--primary-color)}
  .toolbar{display:flex;gap:10px;margin-bottom:10px;padding:12px}.filters{display:grid;grid-template-columns:repeat(7,minmax(110px,1fr)) auto;gap:10px;margin-bottom:10px;padding:12px}.search{flex:1;min-width:190px;display:flex;align-items:center;gap:8px;border:1px solid var(--divider-color);border-radius:9px;padding:0 11px}.search input{border:0;background:transparent;width:100%;outline:0;height:40px}select,input,textarea{border:1px solid var(--divider-color);background:var(--card-background-color);border-radius:8px;padding:10px;outline:none}select:focus,input:focus,textarea:focus{border-color:var(--primary-color);box-shadow:0 0 0 2px color-mix(in srgb,var(--primary-color) 18%,transparent)}.bulk-toolbar{padding:10px 12px;margin-bottom:14px;display:flex;align-items:center;gap:16px}.bulk-toolbar>label{display:flex;align-items:center;gap:7px;font-size:12px}.bulk-toolbar input,.select-cell input{width:17px;height:17px;accent-color:var(--primary-color)}.bulk-toolbar>span{font-size:12px;color:var(--secondary-text-color)}.bulk-toolbar>div{display:flex;gap:8px;margin-left:auto}.bulk-toolbar.active{border-color:color-mix(in srgb,var(--primary-color) 55%,var(--divider-color));background:color-mix(in srgb,var(--primary-color) 5%,var(--card-background-color))}.table-card{overflow:hidden}.table-scroll{overflow:visible}table{width:100%;table-layout:fixed;border-collapse:collapse;font-size:13px}th{text-align:left;color:var(--secondary-text-color);font-size:11px;text-transform:uppercase;letter-spacing:.35px;background:var(--secondary-background-color);padding:12px}th:nth-child(1){width:42px}th:nth-child(2){width:72px}th:nth-child(3){width:25%}th:nth-child(4){width:22%}th:nth-child(5){width:27%}th:nth-child(6){width:110px}th:nth-child(7){width:150px}td{padding:12px;border-top:1px solid var(--divider-color);overflow-wrap:anywhere;vertical-align:top}.select-cell{padding-right:0}.mono{font-family:ui-monospace,monospace;font-size:12px}.pill{display:inline-flex;border-radius:20px;padding:4px 9px;background:color-mix(in srgb,var(--pill) 14%,transparent);color:var(--pill);font-size:12px;font-weight:650}.row-actions{display:flex;justify-content:flex-end}.row-actions button,.row-actions a,.modal-head button,.danger-icon{width:36px;height:36px;border-radius:8px;display:grid;place-items:center;color:inherit;text-decoration:none}.row-actions button:hover,.row-actions a:hover,.modal-head button:hover{background:var(--secondary-background-color)}.danger-icon{color:var(--error-color,#dc2626)}.address-cell>span{white-space:normal}.ip-warning,.duplicate-warning{display:flex;align-items:center;gap:4px;margin-top:5px;font-family:system-ui,sans-serif;font-size:10px;color:#b45309;white-space:normal}.duplicate-warning{color:var(--error-color,#c62828);max-width:280px}.ip-warning button{display:grid;place-items:center;width:24px;height:24px;border-radius:6px;color:inherit}.ip-warning button:hover{background:#fef3c7}.ip-warning ha-icon,.duplicate-warning ha-icon{--mdc-icon-size:14px;flex:0 0 auto}.tag-list{display:flex;gap:4px;flex-wrap:wrap;margin-top:7px}.tag-list span{font:650 10px system-ui,sans-serif;padding:3px 6px;border-radius:10px;background:var(--secondary-background-color);color:var(--secondary-text-color)}
  .section-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px}.section-head h2{margin:0 0 4px}.import-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.import-card{padding:15px;display:flex;align-items:center;gap:13px}.card-actions{display:flex;flex-direction:column;gap:7px;align-items:stretch}.card-actions a{text-decoration:none}.device-icon{width:42px;height:42px;border-radius:11px;background:var(--secondary-background-color);display:grid;place-items:center;color:var(--primary-color)}.unifi-icon{background:#e0f2fe;color:#0284c7}.grow{flex:1;min-width:0}.import-card p{font-size:12px;color:var(--secondary-text-color);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.meta{display:flex;gap:7px;margin-top:8px;align-items:center;flex-wrap:wrap}.meta>span:not(.pill){font-size:11px;color:var(--secondary-text-color)}.empty{padding:50px;text-align:center;color:var(--secondary-text-color)}.empty ha-icon{--mdc-icon-size:42px;margin-bottom:10px}.standalone{background:var(--card-background-color);border-radius:14px}.discover-empty button{margin-top:18px}
  .device-name{display:flex;align-items:center;gap:7px}.unifi-badge{display:inline-flex;align-items:center;gap:3px;border-radius:20px;padding:3px 7px;background:#e0f2fe;color:#0369a1;font-size:10px;font-weight:750}.unifi-badge ha-icon{--mdc-icon-size:13px}.integration-card{display:flex;align-items:flex-start;gap:16px}.integration-logo{width:54px;height:54px;flex:0 0 54px;border-radius:14px;background:#e0f2fe;color:#0284c7;display:grid;place-items:center}.integration-logo ha-icon{--mdc-icon-size:30px}.integration-title{display:flex;align-items:center;gap:10px}.integration-title h2{margin:0}.status-dot{font-size:11px;font-weight:700;padding:4px 8px;border-radius:20px;background:var(--secondary-background-color);color:var(--secondary-text-color)}.status-dot.ok{background:#d1fae5;color:#047857}.inline-form{display:flex;align-items:end;gap:10px;margin:16px 0 8px}.inline-form label{display:grid;gap:6px;flex:1;max-width:520px;font-size:12px;color:var(--secondary-text-color)}.inline-form input,.inline-form select{width:100%}.doc-link{display:inline-flex;align-items:center;gap:5px;color:var(--primary-color);font-size:12px;margin-top:12px;text-decoration:none}.doc-link ha-icon{--mdc-icon-size:14px}.integration-actions{display:flex;gap:8px}.danger-text{color:var(--error-color,#c62828)}.inline-error{color:var(--error-color,#c62828);font-size:12px;margin-top:8px}.details-modal{width:min(600px,100%)}.detail-list{padding:8px 20px 22px}.detail-list>div{display:grid;grid-template-columns:150px 1fr;gap:15px;padding:12px 0;border-bottom:1px solid var(--divider-color)}.detail-list span{font-size:12px;color:var(--secondary-text-color)}.detail-list strong{font-size:13px;overflow-wrap:anywhere}
  .settings-card{margin-bottom:14px}.general-settings{max-width:760px;padding:0;overflow:hidden}.general-settings>label{display:grid;grid-template-columns:minmax(0,1fr) 260px;align-items:center;gap:28px;padding:18px 20px;border-bottom:1px solid var(--divider-color)}.general-settings>label>span{display:grid;gap:5px}.general-settings>label strong{font-size:14px}.general-settings>label small,.format-preview small{color:var(--secondary-text-color);font-size:11px}.general-settings select{width:100%}.format-preview{display:flex;align-items:center;gap:12px;padding:18px 20px;background:color-mix(in srgb,var(--primary-color) 5%,var(--card-background-color))}.format-preview>ha-icon{--mdc-icon-size:27px;color:var(--primary-color)}.format-preview>span{display:grid;gap:4px}.format-preview strong{font-size:15px}.protocol-settings{display:grid;gap:10px}.protocol-setting{display:grid;grid-template-columns:1fr 1.3fr .7fr .7fr .55fr 40px;gap:10px;align-items:end;padding:12px;border:1px solid var(--divider-color);border-radius:10px}.protocol-setting label,.form-grid label{font-size:12px;color:var(--secondary-text-color);display:grid;gap:6px}.protocol-setting input{width:100%}.protocol-setting input[type=color]{height:41px;padding:5px}.settings-card textarea{width:100%;resize:vertical}.form-actions{display:flex;justify-content:flex-end;margin-bottom:14px}.backup-actions{display:flex;gap:8px}.backup-list>div{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:11px 0;border-top:1px solid var(--divider-color)}.backup-list small{display:block;color:var(--secondary-text-color);margin-top:3px}.log-list{display:grid;gap:10px}.log-entry{display:flex;gap:13px;padding:15px}.log-icon{width:38px;height:38px;flex:0 0 38px;border-radius:10px;background:#dbeafe;color:#2563eb;display:grid;place-items:center}.log-icon.delete{background:#fee2e2;color:#dc2626}.log-icon.restore{background:#ede9fe;color:#7c3aed}.log-title{display:flex;align-items:center;gap:9px;flex-wrap:wrap}.log-title span,.log-entry small{font-size:11px;color:var(--secondary-text-color)}.log-entry p{font-size:12px;margin-top:7px}.change-list{margin-top:9px}.change-list>div{display:grid;grid-template-columns:130px minmax(0,1fr) 20px minmax(0,1fr);gap:7px;align-items:center;padding:5px 0;font-size:11px}.change-list b{font-weight:650}.change-list span{overflow-wrap:anywhere}.change-list ha-icon{--mdc-icon-size:14px;color:var(--secondary-text-color)}
  .modal-backdrop{position:fixed;z-index:20;inset:0;background:#0008;display:grid;place-items:center;padding:18px}.modal{width:min(760px,100%);max-height:92vh;overflow:auto;background:var(--card-background-color);border-radius:16px;box-shadow:0 20px 70px #0006}.modal-head{padding:19px 21px;border-bottom:1px solid var(--divider-color);display:flex;justify-content:space-between}.modal-head h2{margin:0 0 4px}.modal-head p{font-size:12px;color:var(--secondary-text-color)}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:20px}.form-grid input,.form-grid select,.form-grid textarea{width:100%}.form-grid .full{grid-column:1/-1}.form-grid small{min-height:13px}.network-fields{grid-column:1/-1;border:1px solid var(--divider-color);border-radius:10px;padding:12px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.network-fields legend{font-size:12px;color:var(--secondary-text-color);padding:0 5px}.network-fields label:last-child{grid-column:1/-1}.tag-picker{position:relative}.tag-picker summary{list-style:none;border:1px solid var(--divider-color);border-radius:8px;padding:10px;min-height:41px;color:var(--primary-text-color);cursor:pointer}.tag-picker summary::-webkit-details-marker{display:none}.tag-picker[open]>div{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px;margin-top:4px;border:1px solid var(--divider-color);border-radius:8px;background:var(--card-background-color)}.tag-picker label{display:flex;align-items:center;gap:6px;color:var(--primary-text-color)}.tag-picker input{width:auto}.bulk-form{padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:12px}.bulk-field{display:grid;grid-template-columns:92px 1fr;gap:10px;align-items:end}.bulk-field>label:last-child,.bulk-tags>label{display:grid;gap:6px;font-size:12px;color:var(--secondary-text-color)}.apply-check{height:41px;display:flex;align-items:center;gap:6px;font-size:12px}.apply-check input{width:17px;height:17px;accent-color:var(--primary-color)}.bulk-field select,.bulk-field input{width:100%}.bulk-tags{grid-column:1/-1;border-top:1px solid var(--divider-color);padding-top:14px}.bulk-tag-options{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px}.bulk-tag-options label{display:flex;align-items:center;gap:6px;font-size:12px}.bulk-tag-options input{width:17px;height:17px;accent-color:var(--primary-color)}.bulk-tag-options.disabled{opacity:.45}.id-field{display:grid;grid-template-columns:1fr 42px;gap:7px}.id-field button{width:42px;padding:0}.modal-actions{padding:15px 20px;border-top:1px solid var(--divider-color);display:flex;justify-content:flex-end;gap:9px}#toast{position:fixed;z-index:30;left:50%;bottom:30px;transform:translate(-50%,30px);background:#17202a;color:#fff;padding:11px 16px;border-radius:9px;opacity:0;pointer-events:none;transition:.2s}#toast.show{opacity:1;transform:translate(-50%,0)}#toast.error{background:var(--error-color,#c62828)}.state{min-height:70vh;display:flex;align-items:center;justify-content:center;gap:12px;color:var(--secondary-text-color)}.spinner{width:22px;height:22px;border:3px solid var(--divider-color);border-top-color:var(--primary-color);border-radius:50%;animation:spin .8s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
  @media(max-width:900px){.stats{grid-template-columns:repeat(2,1fr)}.grid-two,.import-grid{grid-template-columns:1fr}.toolbar{flex-wrap:wrap}.search{flex-basis:100%}.filters{grid-template-columns:repeat(2,minmax(0,1fr))}.protocol-setting{grid-template-columns:1fr 1fr 1fr}.protocol-setting .danger-icon{align-self:end}.app{padding:18px 14px 50px}.integration-card{flex-wrap:wrap}.integration-actions{width:100%;justify-content:flex-end}}
  @media(max-width:600px){header{align-items:flex-start}header h1{font-size:22px}header .primary{font-size:0;width:42px;padding:0}header .primary ha-icon{font-size:initial}.stats{gap:9px}.stat{padding:13px;gap:10px}.stat-icon{width:38px;height:38px}.stat strong{font-size:20px}.nav{padding:11px 12px}.nav span{font-size:12px}.toolbar .secondary{flex:1;font-size:12px;padding:0 8px}.filters{grid-template-columns:1fr}.bulk-toolbar{align-items:flex-start;flex-wrap:wrap}.bulk-toolbar>div{width:100%;margin-left:0}.bulk-toolbar>div button{flex:1}.form-grid{grid-template-columns:1fr}.form-grid .full,.network-fields,.network-fields label:last-child{grid-column:auto}.network-fields{grid-template-columns:1fr}.tag-picker[open]>div{grid-template-columns:repeat(2,1fr)}.bulk-form{grid-template-columns:1fr}.bulk-tags{grid-column:auto}.bulk-tag-options{grid-template-columns:repeat(2,1fr)}.protocol-setting{grid-template-columns:1fr 1fr}.general-settings>label{grid-template-columns:1fr;gap:10px}.import-card{align-items:flex-start}.import-card .primary{align-self:center}.section-head{align-items:flex-start}.section-head .secondary{font-size:0;width:42px;padding:0}.section-head .secondary ha-icon{font-size:initial}.inline-form{align-items:stretch;flex-direction:column}.inline-form button{width:100%}.detail-list>div{grid-template-columns:1fr;gap:4px}.backup-actions{flex-wrap:wrap;justify-content:flex-end}.change-list>div{grid-template-columns:1fr}.change-list ha-icon{transform:rotate(90deg)}table,thead,tbody,tr,th,td{display:block}thead{display:none}tbody{display:grid;gap:10px;padding:10px}tr{border:1px solid var(--divider-color);border-radius:10px;padding:10px}td{border:0;padding:6px}td:first-child{float:right}.row-actions{justify-content:flex-start}}
  .table-card{border-radius:10px}.table-scroll{overflow:auto;max-height:calc(100vh - 330px);min-height:260px}.device-table{table-layout:fixed;border-collapse:separate;border-spacing:0;font-size:12px}.device-table th{position:sticky;top:0;z-index:3;width:auto;height:43px;padding:0 12px;background:var(--card-background-color);border-bottom:1px solid var(--divider-color);white-space:nowrap;text-transform:none;font-size:11px;letter-spacing:0}.device-table th:not(:last-child),.device-table td:not(:last-child){border-right:1px solid color-mix(in srgb,var(--divider-color) 55%,transparent)}.device-table td{height:45px;padding:8px 12px;border-top:0;border-bottom:1px solid var(--divider-color);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;vertical-align:middle}.device-table .select-head,.device-table .select-cell{position:sticky;left:0;z-index:4;padding:0;text-align:center;background:var(--card-background-color)}.device-table .select-cell{z-index:2}.device-table tbody tr{cursor:pointer;outline:none}.device-table tbody tr:hover td,.device-table tbody tr:hover .select-cell{background:color-mix(in srgb,var(--primary-color) 6%,var(--card-background-color))}.device-table tbody tr.active td,.device-table tbody tr.active .select-cell{background:color-mix(in srgb,var(--primary-color) 12%,var(--card-background-color))}.device-table tbody tr.active td:first-child{box-shadow:inset 3px 0 var(--primary-color)}.device-table .tag-list{margin:0;flex-wrap:nowrap;overflow:hidden}.device-table .tag-list span{flex:0 0 auto}.device-name-cell strong{display:inline-block;max-width:calc(100% - 18px);overflow:hidden;text-overflow:ellipsis;vertical-align:middle}.unifi-dot{display:inline-block;width:7px;height:7px;margin-left:7px;border-radius:50%;background:#0ea5e9;vertical-align:middle}.column-resizer{position:absolute;z-index:5;top:0;right:-4px;width:9px;height:100%;cursor:col-resize;touch-action:none}.column-resizer:hover,.column-resizer:active{background:color-mix(in srgb,var(--primary-color) 45%,transparent)}.device-status{display:inline-flex;align-items:center;gap:6px;text-transform:capitalize}.device-status i{width:7px;height:7px;border-radius:50%;background:#94a3b8}.device-status.online i{background:#22c55e}.device-status.offline i{background:#ef4444}
  .toolbar{align-items:center;flex-wrap:wrap}.toolbar>select{max-width:180px}.icon-button{width:42px;padding:0}.columns-menu{position:relative}.columns-menu>summary{list-style:none;cursor:pointer}.columns-menu>summary::-webkit-details-marker{display:none}.columns-popover{position:absolute;z-index:20;top:48px;right:0;width:340px;padding:12px;border:1px solid var(--divider-color);border-radius:12px;background:var(--card-background-color);box-shadow:0 14px 38px #0003}.column-list{display:grid;gap:3px;max-height:390px;overflow:auto}.column-option{display:grid;grid-template-columns:24px minmax(0,1fr) 34px;align-items:center;gap:7px;min-height:38px;padding:3px 4px;border-radius:8px}.column-option:hover{background:var(--secondary-background-color)}.column-option.dragging{opacity:.4}.drag-handle{--mdc-icon-size:18px;color:var(--secondary-text-color);cursor:grab}.column-option label{display:flex;align-items:center;gap:8px;font-size:12px}.column-option input{width:16px;height:16px;accent-color:var(--primary-color)}.pin-column{width:32px;height:32px;border-radius:7px;color:var(--secondary-text-color)}.pin-column.active{color:var(--primary-color);background:color-mix(in srgb,var(--primary-color) 12%,transparent)}.density-setting{display:grid;grid-template-columns:1fr repeat(3,auto);align-items:center;gap:4px;margin:10px 0;padding-top:10px;border-top:1px solid var(--divider-color);font-size:11px;color:var(--secondary-text-color)}.density-setting button{padding:7px;border-radius:7px}.density-setting button.active{background:var(--primary-color);color:#fff}.reset-columns{width:100%}
  .device-table th>button{width:calc(100% - 8px);height:100%;display:flex;align-items:center;justify-content:space-between;gap:6px;text-align:left;font-weight:700;color:inherit}.device-table th>button ha-icon{--mdc-icon-size:15px;color:var(--secondary-text-color)}.device-table.density-compact td{height:37px;padding-top:5px;padding-bottom:5px}.device-table.density-comfortable td{height:55px;padding-top:12px;padding-bottom:12px}.device-table .pinned-column{position:sticky;z-index:2;background:var(--card-background-color)}.device-table th.pinned-column{z-index:4}.device-table .select-head{z-index:5}.device-table .select-cell{z-index:3}.device-name-cell{display:inline-flex;align-items:center;max-width:100%;gap:6px}.child-device-icon{--mdc-icon-size:15px;color:var(--secondary-text-color);flex:0 0 auto}.copy-cell{width:26px;height:26px;margin-left:5px;border-radius:6px;vertical-align:middle;opacity:0;color:var(--secondary-text-color)}td:hover>.copy-cell,.copy-cell:focus{opacity:1}.copy-cell:hover{background:var(--secondary-background-color);color:var(--primary-color)}.copy-cell ha-icon{--mdc-icon-size:14px}
  .battery-fields{grid-column:1/-1;border:1px solid var(--divider-color);border-radius:10px;padding:12px;display:grid;grid-template-columns:1.5fr 1fr;gap:12px}.battery-fields legend{font-size:12px;color:var(--secondary-text-color);padding:0 5px}.battery-fields label{display:grid;gap:6px;font-size:12px;color:var(--secondary-text-color)}.battery-fields select,.battery-fields input{width:100%}.battery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}.battery-card{padding:17px;cursor:pointer;transition:transform .15s ease,border-color .15s ease}.battery-card:hover{transform:translateY(-2px);border-color:color-mix(in srgb,var(--primary-color) 45%,var(--divider-color))}.battery-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;padding-bottom:15px}.battery-card h3{font-size:16px;margin:5px 0 4px}.battery-card p{font-size:12px;color:var(--secondary-text-color)}.battery-card-details{display:grid;gap:8px;padding:13px 0;border-top:1px solid var(--divider-color);border-bottom:1px solid var(--divider-color)}.battery-card-details>div{display:grid;grid-template-columns:125px minmax(0,1fr);gap:10px}.battery-card-details span{font-size:11px;color:var(--secondary-text-color)}.battery-card-details strong{font-size:11px;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.battery-card-actions{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:13px}.battery-health{font-size:10px;font-weight:750;text-transform:uppercase;letter-spacing:.45px}.battery-health.good{color:#059669}.battery-health.medium{color:#d97706}.battery-health.low{color:#dc2626}.battery-health.unknown{color:var(--secondary-text-color)}.battery-indicator{display:inline-flex;align-items:center;gap:5px;font-size:11px}.battery-indicator ha-icon{--mdc-icon-size:20px}.battery-indicator.large{padding:7px 9px;border-radius:9px;background:var(--secondary-background-color);font-size:14px}.battery-indicator.large ha-icon{--mdc-icon-size:26px}.battery-indicator.good{color:#059669}.battery-indicator.medium{color:#d97706}.battery-indicator.low{color:#dc2626}.battery-indicator.unknown{color:var(--secondary-text-color)}.drawer-section-title{display:flex!important;grid-template-columns:none!important;align-items:center;justify-content:space-between;padding:0 0 7px!important}.drawer-section-title h3{margin:0!important}.battery-action{color:var(--primary-color);background:color-mix(in srgb,var(--primary-color) 10%,var(--card-background-color))}.battery-history{display:block!important;margin-top:15px;padding-top:13px!important;border-top:1px solid var(--divider-color)!important}.battery-history h4{margin:0 0 10px;font-size:12px}.battery-history>div{display:grid!important;grid-template-columns:12px 1fr!important;gap:8px!important;padding:6px 0!important;border:0!important}.battery-history i{width:8px;height:8px;margin-top:4px;border-radius:50%;background:var(--primary-color)}.battery-history span{display:block!important}.battery-history strong{display:block;text-align:left!important}.battery-history small{display:block;margin-top:2px;color:var(--secondary-text-color)}.battery-modal{width:min(540px,100%)}
  .device-drawer{position:fixed;z-index:25;top:0;right:0;bottom:0;width:min(440px,100vw);display:flex;flex-direction:column;background:var(--card-background-color);border-left:1px solid var(--divider-color);box-shadow:-14px 0 40px #0003;transform:translateX(105%);transition:transform .2s ease}.device-drawer.open{transform:translateX(0)}.drawer-head{padding:22px 20px 18px;border-bottom:1px solid var(--divider-color);display:flex;align-items:flex-start;justify-content:space-between;gap:15px}.drawer-head h2{font-size:21px;margin:5px 0 10px}.drawer-head>button{width:38px;height:38px;display:grid;place-items:center;border-radius:8px}.drawer-head>button:hover{background:var(--secondary-background-color)}.drawer-badges{display:flex;align-items:center;gap:7px;flex-wrap:wrap}.drawer-body{flex:1;overflow:auto;padding:14px 20px 24px}.drawer-body section{margin-bottom:14px;padding:16px;border:1px solid var(--divider-color);border-radius:12px;background:color-mix(in srgb,var(--secondary-background-color) 42%,var(--card-background-color))}.drawer-body section h3{margin-bottom:11px}.drawer-body section>div:not(.tag-list){display:grid;grid-template-columns:135px minmax(0,1fr);gap:12px;padding:8px 0;border-bottom:1px solid color-mix(in srgb,var(--divider-color) 75%,transparent)}.drawer-body section>div:last-of-type{border-bottom:0}.drawer-body section span{font-size:11px;color:var(--secondary-text-color)}.drawer-body section strong{font-size:12px;text-align:right;overflow-wrap:anywhere}.drawer-body .tag-list{margin-top:12px}.drawer-inline-action{width:100%;margin-top:12px;padding:9px;border-radius:8px;display:flex;align-items:center;justify-content:center;gap:7px;color:#b45309;background:#fef3c7}.drawer-warning{display:flex;align-items:flex-start;gap:6px;margin-top:10px;color:var(--error-color,#c62828);font-size:11px}.drawer-warning ha-icon{--mdc-icon-size:16px;flex:0 0 auto}.drawer-actions{padding:14px 16px;border-top:1px solid var(--divider-color);display:flex;justify-content:flex-end;gap:8px;background:var(--card-background-color)}.drawer-actions .drawer-icon-action{width:42px;padding:0;text-decoration:none}.drawer-actions .primary{flex:1}.drawer-scrim{display:none;position:fixed;z-index:24;inset:0;background:#0006}
  @media(max-width:900px){.table-scroll{max-height:calc(100vh - 390px)}.drawer-scrim.open{display:block}}
  @media(max-width:600px){.device-table{display:table}.device-table thead{display:table-header-group}.device-table tbody{display:table-row-group;padding:0}.device-table tr{display:table-row;border:0;padding:0}.device-table th,.device-table td{display:table-cell}.device-table thead{display:table-header-group}.device-table td:first-child{float:none}.table-scroll{max-height:calc(100vh - 470px)}.drawer-head{padding-top:18px}.drawer-actions .secondary:not(.drawer-icon-action){font-size:0;width:42px;padding:0}.drawer-actions .secondary ha-icon{font-size:initial}}
  @media(max-width:600px){.battery-fields{grid-template-columns:1fr}.battery-grid{grid-template-columns:1fr}.battery-card-details>div{grid-template-columns:105px minmax(0,1fr)}.battery-card-actions{align-items:flex-start;flex-direction:column}.battery-card-actions button{width:100%}}
`;

customElements.define("network-inventory-panel", NetworkInventoryPanel);
