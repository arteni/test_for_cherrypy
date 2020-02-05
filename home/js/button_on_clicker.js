updater_switcher()
updater_sensors()
var refreshIntervalId = setInterval(updater_switcher, 1000);
var refreshIntervalIdSensors = setInterval(updater_sensors, 2000);
window.onload = refreshIntervalId

function updater_sensors(){
    jQuery.ajax({
        url:window.location["href"]+"api/v1/sens", success:function(result){
            sensors = JSON.parse(JSON.stringify(result))
            for(id in sensors){
                    document.getElementById(id).remove
                    document.getElementById(id).innerHTML = sensors[id]
                }
            }
    })
}

function updater_switcher(){
        jQuery.ajax({
            url:window.location["href"]+"api/v1/state", success:function(result){
                switcher = JSON.parse(JSON.stringify(result))
                for(id in switcher){
                    document.getElementById(id).remove
                    document.getElementById(id).innerHTML = switcher[id]
                }
            }
        });
    }

function isEmpty(str) {
  if (str.trim() == '')
    return true;
  return false;
}

function change(str) {
  if (str == 'on')
    return "off";
  else if (str == "off")
    return "on";
}