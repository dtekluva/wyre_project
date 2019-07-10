var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/'
    
///////////////////////////////////////////////////////////////////////////
///////////////////                                     ///////////////////
/////////////////  JAVASCRIPT FILTER BY BRANCH AND TIME  //////////////////
///////////////////                                     ///////////////////
///////////////////////////////////////////////////////////////////////////

total_kw = document.getElementById("total_kw")
min_kw = document.getElementById("min_kw")
peak_kw = document.getElementById("peak_kw")
avg_kw = document.getElementById("avg_kw")

console.log(total_kw)
    
$('#branch').on('change', async e => {
    let branch = $("#branch")[0].value
    let period = $("#time_period")[0].value
    post(branch, period);
})
$('#time_period').on('apply.daterangepicker', async e => {
    let branch = $("#branch")[0].value
    let period = $("#time_period")[0].value
    post(branch, period);
})

const post = (branch, period)=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  console.log(period)

  let data = {"branch": branch,
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

  $.post(host + 'fetch_vals_period/', data)
        .then(resp => {
          resp = JSON.parse(resp)
          
          if (resp.response == 'success') {
            // alert("Feature in progress");
            total_kw.innerHTML = `Total Energy ${resp.data.energy_used}-kwh`;
            peak_kw.innerHTML = resp.data.peak_kw;
            min_kw.innerHTML = resp.data.min_kw;
            avg_kw.innerHTML = resp.data.avg_kw;
            console.log(resp)
          } else if (resp.response == 'failure') {
            $("#login_error").show()
          }
        })
        .catch(() => {
          text = {
            title: "Network Error",
            text: `Please check your internet connection.!!`,
            icon: "error"
          };
        }) // post data


}