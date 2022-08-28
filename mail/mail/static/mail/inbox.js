document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').onsubmit = send_email;
  document.querySelector('#compose-form2').onsubmit = send_reply;
  // By default, load the inbox
  load_mailbox('inbox');


});



function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#reply-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  
}


function send_email()
{
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  //console.log(recipients)

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body,
    })
  })
  .then(response => response.json())
      .then(result => {
        if ("message" in result) {
            // The email was sent successfully!
            load_mailbox('sent');
        }

        if ("error" in result) {
            // There was an error in sending the email
            // Display the error next to the "To:"
            document.querySelector('#to-text-error-message').innerHTML = result['error']

        }
        console.log(result);
        console.log("message" in result);
        console.log("error" in result);
      })
        .catch(error => {
            // we hope this code is never executed, but who knows?
            console.log(error);
        });
  return false;
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#reply-view').style.display = 'none';
  

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  if(mailbox=="inbox")
  {
    fetch('/emails/inbox')
      .then(response => response.json())
        .then(emails => {
        // Print emails
        emails.forEach(email => {
        //if archived is false then show that email
        if(email.archived==false)
        {
          console.log(email.sender);
          console.log(email.recipients);
          console.log(email.id);
          console.log(email.archived);
          console.log(email.read);

          var item = document.createElement("div");
          item.className = 'card-body';
          item.innerHTML = `<div>  ${email.sender} | ${email.subject} | ${email.timestamp}  <button onclick="Archived(${email.id})" type="button" style="float:right" class="btn btn-info">Archive</button></div>`;
          
          
          var matter = document.createElement("div");
          if(email.read==true)
          {
            matter.className = "card bg-light text-dark";
          }
          else
          {
            matter.className = "card bg-secondary text-white";
          }
          matter.id = "emailone";
          matter.style.margin = "10px";
          
          matter.appendChild(item);
          

          document.querySelector("#emails-view").appendChild(matter);
        

          matter.addEventListener("click", () => {

            //Element is clicked so it should be marked as read
            make_read(email.id);
            view_email(email.id);
          })
        }
        });
        
      // ... do something else with emails ...
        
});
  }
  //Mailbox == sent
  else if(mailbox=="sent")
  {
    fetch('/emails/sent')
      .then(response => response.json())
        .then(emails => {
        // Print emails
        emails.forEach(email => {
        
          console.log(email.sender);
          console.log(email.recipients);
          console.log(email.id);
          console.log(email.archived);
          console.log(email.read);

          var item = document.createElement("div");
          item.className = 'card-body';
          item.innerHTML = `<div>  ${email.sender} | ${email.subject} | ${email.timestamp} </div>`;
          
          
          var matter = document.createElement("div");
          if(email.read==true)
          {
            matter.className = "card bg-light text-dark";
          }
          else
          {
            matter.className = "card bg-secondary text-white";
          }
          matter.id = "emailone";
          matter.style.margin = "10px";
          
          matter.appendChild(item);
          

          document.querySelector("#emails-view").appendChild(matter);
        

          matter.addEventListener("click", () => {

            //Element is clicked so it should be marked as read
            make_read(email.id);
            view_email(email.id);
          })
        });
      // ... do something else with emails ...
        });
  }
  else if(mailbox=="archive")
  {
    fetch('/emails/archive')
      .then(response => response.json())
        .then(emails => {
        // Print emails
        emails.forEach(email => {
        //if archived is true then show that email
        if(email.archived==true)
        {
          console.log(email.sender);
          console.log(email.recipients);
          console.log(email.id);
          console.log(email.archived);
          console.log(email.read);

          var item = document.createElement("div");
          item.className = 'card-body';
          item.innerHTML = `<div>  ${email.sender} | ${email.subject} | ${email.timestamp}  <button onclick="Unarchived(${email.id})" type="button" style="float:right" class="btn btn-info">Unarchive</button></div>`;
          
          
          var matter = document.createElement("div");
          if(email.read==true)
          {
            matter.className = "card bg-light text-dark";
          }
          else
          {
            matter.className = "card bg-secondary text-white";
          }
          matter.id = "emailone";
          matter.style.margin = "10px";
          
          matter.appendChild(item);
          

          document.querySelector("#emails-view").appendChild(matter);
        

          matter.addEventListener("click", () => {

            //Element is clicked so it should be marked as read
            make_read(email.id);
            view_email(email.id);
          })
        }
        });
      // ... do something else with emails ...
        });
  }
}

function Archived(id)
{
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: true,
    })
  });
  console.log("Email archived");
  
  event.stopPropagation();
  location.reload()
}

function Unarchived(id)
{
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: false,
    })
  });
  console.log("Email Unarchived");
  
  event.stopPropagation();
  location.reload()
}

function make_read(id) {
  fetch(`/emails/${id}`, {
    method: "PUT",
    body: JSON.stringify({
      read: true,
    }),
  });
}

function view_email(id)
{
  //hide all views except single email view
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'block';
  document.querySelector('#reply-view').style.display = 'none';


  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      // ... do something else with email ...
      var view = document.createElement('div');
      view.innerHTML = `<div> <h3>Sender: ${email.sender}</h3> <br> <h3>Receiver: ${email.recipients}</h3> <br> <h3>Subject: ${email.subject}</h3> <br> <h3>Timestamp: ${email.timestamp}</h3> <br> <h3>Body:<h4> ${email.body}</h4></h3><br></div>`;
      var butto = document.createElement('div');
      butto.innerHTML = `<div><button onclick="composeReply(${id})" type="button" class="btn btn-primary">Reply</button></div>`

      document.querySelector("#single-email-view").innerHTML = '';
      document.querySelector("#single-email-view").appendChild(view);
      document.querySelector("#single-email-view").appendChild(butto);
  });
}

function composeReply(id){

  
  //hide all views except reply view
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#reply-view').style.display = 'block';

  //clear body field
  document.querySelector('#compose-body2').value = '';
   
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      // ... do something else with email ...
       // Clear out composition fields
  document.querySelector('#compose-recipients2').value = email.sender;
  if(email.subject.slice(0,4)=="Re: ")
  {
    document.querySelector('#compose-subject2').value = email.subject;
  }
  else
  {
    document.querySelector('#compose-subject2').value = "Re: " + email.subject;  
  }
  document.querySelector('#compose-body2').value = "On "+ email.timestamp + " " + email.sender +" wrote: " + email.body + " ============================";

  });
}

function send_reply()
{
  const recipients = document.querySelector('#compose-recipients2').value;
  const subject = document.querySelector('#compose-subject2').value;
  const body = document.querySelector('#compose-body2').value;
  //console.log(recipients)

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body,
    })
  })
  .then(response => response.json())
      .then(result => {
        if ("message" in result) {
            // The email was sent successfully!
            load_mailbox('sent');
        }

        if ("error" in result) {
            // There was an error in sending the email
            // Display the error next to the "To:"
            document.querySelector('#to-text-error-message').innerHTML = result['error']

        }
        console.log(result);
        console.log("message" in result);
        console.log("error" in result);
      })
        .catch(error => {
            // we hope this code is never executed, but who knows?
            console.log(error);
        });
  return false;
}