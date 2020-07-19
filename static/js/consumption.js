var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

if (location.protocol === 'https:') {
  // page is secure
  host = host.replace("http", "https")
}
    
const endpoint = "get_energy_consumption_readings/";
var table;
var values = {"data":{}}
///////////////////////////////////////////////////////////////////////////
///////////////////                                     ///////////////////
/////////////////  JAVASCRIPT FILTER BY device AND TIME  //////////////////
///////////////////                                     ///////////////////
///////////////////////////////////////////////////////////////////////////


    
$('#device').on('change', async e => {
  let device = $("#device")[0].value;
  let period = get_daterange();
  let resolution = $("#resolution")[0].value;

  post(device, period, resolution);
})

$('#resolution').on('change', async e => {
  let device = $("#device")[0].value;
  let period = get_daterange();
  let resolution = $("#resolution")[0].value;

  post(device, period, resolution);
})


$(function() {
  $('input[name="consumption_dates"]').daterangepicker({
    timePicker: false,
    startDate: moment().startOf('hour'),
    endDate: moment().startOf('hour').add(32, 'hour'),
    locale: {
      format: 'M/DD/YYYY'
    }
  });
});

//LOAD DATEPICKER ONCHANGE EVENT
$('input[name="consumption_dates"]').on('apply.daterangepicker', async e => {

  let device = $("#device")[0].value;
  let period = get_daterange();
  let resolution = $("#resolution")[0].value;

  post(device, period, resolution);

});


$(window).on('load', function() {

  let device = $("#device")[0].value;
  let period = get_daterange();
  let resolution = $("#resolution")[0].value;

  table = $('#reaing_table').DataTable( {
                "scrollX": true,
                dom: 'Brtip',
                buttons: [
                    'copy', 'csv', 'excel', 'pdf', '# print'
                    
                ],
                "columnDefs": [
                  {"className": "dt-center", "targets": "_all"}
                ],
                "pageLength": 20
              } );
  post(device, period, resolution);
});

const post = (device, period, resolution)=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  let data = {
              "device": device,
              "date": period,
              "resolution": resolution
              }; // add lives_in select value to post data
  
  function csrfSafeMethod (method) {
        // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
  }

  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken)
      }
    }
  })
  
  $.post(host + endpoint, data)
        .then(resp => {
          resp = JSON.parse(resp)
          values.data = resp.data;
          
          if (resp.response == 'success') {
            
              populate_data(prepare_data());
              add_to_tables(values);            
            
          } else if (resp.response == 'failure') {
            swal({
                  title: "Error fetching data!!",
                  text: "Something went wrong",
                });
          }
        })
        .catch(() => {
          text = {
            title: "Network Error",
            text: `Please check your internet connection.!!`,
            icon: "error"
          };
          swal({
            title: "Network Error",
            text: "Please check your internet connection.!!",
          });
        }) // post data
}


function populate_data(data){
    
    ActivityChart.chart.data.datasets[0].data = data.kwh;
    ActivityChart.chart.data.datasets[0].label = "kW⋅h";
    ActivityChart.chart.data.labels = data.timestamp;
    ActivityChart.update();
}

function prepare_data(){
  let kwh = [];
  let timestamp = [];

  values.data.forEach(element => {
    timestamp.push(element[0]);
    kwh.push(element[1]);
  });

  return {'timestamp':timestamp,'kwh':kwh}
};

function time_convert (time) {
  // Check correct time format and split into components
  time = time.slice(0,8)
  time = time.toString().match (/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];

  if (time.length > 1) { // If time format correct
    time = time.slice(1);  // Remove full string match value
    time[5] = +time[0] < 12 ? 'AM' : 'PM'; // Set AM/PM
    time[0] = +time[0] % 12 || 12; // Adjust hours
  }
  return time.join (''); // return adjusted time or original string
}

function add_to_tables(values){
  table.clear().draw()
  let i = 0;
  values.data.forEach(element => {
    i ++;
    table.row.add( [
      i,
      element[0],
      element[1],
      "-",
      "-",
      "-",
      "-",
      "-",
      "-",
      "-",
      "-",
      "-",
  ] )
  Swal.close()
});
    
 table.draw();
};

function todays_date(){
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  today = mm + '/' + dd + '/' + yyyy;
  return today
}

// ADD THE ABILITY TO REMOVE ONE HOUR FROM A TIME OBJECT TO JS TIME CLASS
Date.prototype.remHours = function(h) {  
  this.setTime(this.getTime() - (h*60*60*1000));
  return this;
}


var get_daterange = (()=>{
  let start_date = $('input[name="consumption_dates"]').data('daterangepicker').startDate.format('MM/DD/YYYY');
  let end_date = $('input[name="consumption_dates"]').data('daterangepicker').endDate.format('MM/DD/YYYY');

  return `${start_date}-${end_date}`;
});