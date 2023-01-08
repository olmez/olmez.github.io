# Python
def handle_form_submission(request):
  name = request.form['name']
  email = request.form['email']
  message = request.form['message']
  # Save the form submission to a database or send an email, for example
  return redirect('/thank-you')
