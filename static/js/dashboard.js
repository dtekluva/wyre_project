var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/'
    
///////////////////////////////////////////////////////////////////////////
///////////////////                                     ///////////////////
/////////////////  JAVASCRIPT FILTER BY BRANCH AND TIME  //////////////////
///////////////////                                     ///////////////////
///////////////////////////////////////////////////////////////////////////

$('#branch').on('change', async e => {
  console.log(e.target.value)
})



    
$('#branch').on('change', async e => {
    let branch = e.target.value
    console.log(branch)
    post(branch)
    
})

const post = (branch)=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  console.log(csrftoken)

  let data = {branch}; // add lives_in select value to post data

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
            alert("done");
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