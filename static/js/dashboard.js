var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/'
    
var endpoint = "fetch_vals_period/";
var usage_difference = "get_yesterday_today_usage/"
///////////////////////////////////////////////////////////////////////////
///////////////////                                     ///////////////////
/////////////////  JAVASCRIPT FILTER BY device AND TIME  //////////////////
///////////////////                                     ///////////////////
///////////////////////////////////////////////////////////////////////////

total_kw = document.getElementById("total_kw");
min_kw = document.getElementById("min_kw");
peak_kw = document.getElementById("peak_kw");
avg_kw = document.getElementById("avg_kw");
today_usage = document.getElementById("today_usage");
yesterday_usage = document.getElementById("yesterday_usage");


$(window).on('load', function() {
  let device = $("#device")[0].value;
  // console.log(device)
  let period = $("#default_range")[0].innerHTML;
  get_usage_difference("None");
  post(device, period);
});
    
$('#device').on('change', async e => {
    let device = $("#device")[0].value;
    let period = $("#time_period")[0].value;
    get_usage_difference(device);
    post(device, period);
});

$('#time_period').on('apply.daterangepicker', async e => {
    let device = $("#device")[0].value;
    let period = $("#time_period")[0].value;
    post(device, period);
});

const post = (device, period)=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  // console.log(period)

  let data = {
              "device": device,
              "period": period
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
          console.log(resp);
          if (resp.response == 'success') {
              // alert("Feature in progress");
              total_kw.innerHTML = `${resp.data.energy_used} kwh`;
              peak_kw.innerHTML = resp.data.peak_kw;
              min_kw.innerHTML = resp.data.min_kw;
              avg_kw.innerHTML = resp.data.avg_kw;
              days = resp.data.daily_device_usage.days;
              utility = resp.data.daily_device_usage.utility;
              gen1 = resp.data.daily_device_usage.gen1;
              gen2 = resp.data.daily_device_usage.gen2;
              utility_hrs = resp.data.utility_times;
              gen1_hrs = resp.data.gen1_times;
              gen2_hrs = resp.data.gen2_times;
              addData(DiseasesChart, utility_hrs, gen1_hrs, gen2_hrs);
              
              if (endpoint == "fetch_vals_period/"){
                  addData(DiseasesChart, utility_hrs, gen1_hrs, gen2_hrs); 
                  update_bar_chart(ActivityChart, days, utility, gen1, gen2);                
              }else{
                update_bar_chart(ActivityChart, days, utility, gen1, gen2);
              };

              endpoint = "fetch_device_vals/";
            
          } else if (resp.response == 'failure') {
            swal({
                  title: "Error fetching data!!",
                  text: "Try selecting a valid date range first",
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
};

const get_usage_difference = (device)=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  // console.log(period)

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
  let data = {
    "device": device
    };
  
  $.post(host + usage_difference, data)
        .then(resp => {
          resp = JSON.parse(resp)
          console.log(resp);

          if (resp.response == 'success') {

            yesterday_usage.innerHTML = resp.data.yesterday_energy;
            today_usage.innerHTML = resp.data.today_energy;

          } else if (resp.response == 'failure') {
            swal({
                  title: "Error fetching data!!",
                  text: "An error occurred",
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


function addData(chart, utility, gen1, gen2) {
  chart.data.datasets.forEach((dataset) => {
      dataset.data = [gen1, gen2, utility];
  });
  chart.update();
}

function update_bar_chart(chart, days, utility, gen1, gen2) {
  chart.data.labels = days;
  chart.data.datasets[0].data = utility;
  console.log(sum(gen2))
  chart.data.datasets[1].data = gen1;
  chart.data.datasets[2].data = gen2;
  chart.update();
}

function sum(input){
             
  if (toString.call(input) !== "[object Array]")
     return false;
       
             var total =  0;
             for(var i=0;i<input.length;i++)
               {                  
                 if(isNaN(input[i])){
                 continue;
                  }
                   total += Number(input[i]);
                }
              return total;
             }