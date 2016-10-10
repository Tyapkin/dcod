function initRegionDdList() {
  $('#region-dd-list select').change(function(event) {
    var region_id = $(this).val();

    if (region_id) {
      $.cookie('current_region', region_id, {'path': '/', 'expires': 365});
    } else {
      $.removeCookie('current_region', {'path': '/'});
    }

    location.reload(true);

    return true;
  });
}

$(document).ready(function() {
  initRegionDdList();
});