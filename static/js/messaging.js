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

message_list = document.getElementById("message_list");
message_box = document.getElementById("message_box");

var show = ()=> message_box.removeAttribute("hidden");
var hide = ()=> message_box.setAttribute("hidden", true);




$(window).on('load', function() {
  let device = $("#device")[0].value;
  message_list.addEventListener("click", (e)=>{
    show()
    show = [hide, hide = show][0];
  })
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
             
              
              if (endpoint == "fetch_vals_period/"){
                                 
              }else{
                
              };

              endpoint = "fetch_device_vals/";
            
          }else if (resp.response == 'failure') {
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