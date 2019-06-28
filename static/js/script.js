var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/'
console.log(host)
    
$('#LoginForm').on('submit', async e => {
    e.preventDefault()
    let data = $('#LoginForm') // add lives_in select value to post data
    console.log(data)
    post()
    
})

const post = ()=>{
  let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
  console.log(csrftoken)
  let page = 'login'

  let form_data = `${$('#LoginForm').serialize()}` // add lives_in select value to post data

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

  $.post(host + 'auth/'+ page , form_data)
        .then(resp => {
          resp = JSON.parse(resp)
          console.log(resp)

          if (resp.response == 'success') {
            window.location.replace('/')
          } else if (resp.response == 'fail') {
            text = {
                      title: "Possible Duplicate error",
                      text: `User with similar record possibly exists. Please confirm`,
                      icon: "error",
                    }
          }
        })
        .catch(() => {
          text = {
            title: "Network Error",
            text: `Please check your internet connection.!!`,
            icon: "error",
          };
        }) // post data


}