function initRegionDdList() {
  $('#region-dd-list select').change(function(event) {
    var region = $(this).val();

    if (region) {
      $.cookie('current_region', region, {'path': '/', 'expires': 365});
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