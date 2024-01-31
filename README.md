# converter-bot
Discord Bot that converts imperial &amp; metrics

<h1>Local set up</h1>

Clone GitHub repo
Create bot in the Discord Developer Portal and get the token + client ID of the bot
You can invite your bot to a server with this link (including the needed permissions): <code>https://discord.com/api/oauth2/authorize?client_id=<CLIENT_ID>&permissions=277025405952&scope=bot</code>
Fill in your token in the .env file
Run <code>app.py</code>

<h2>Supported slash commands</h2>

<code>/milestokm</code> : convert miles, yard, feet, inches into km, m, cm
<code>/kmtomiles</code> : convert km, m, cm into miles, yard, feet, inches
<code>/ftoc</code> : convert fahrenheit to celsius
<code>/ctof</code> : convert celsius to fahrenheit
<b>-- all values are currently mandatory to fill in</b>