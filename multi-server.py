server_list = []
spam_head = '¡El rico spam viene!'
spam_var = 'Es hora del spam!\nEstos son los súper canales de YouTube que apoyamos y TENES que suscribirte.\nhttps://www.youtube.com/channel/UCOiUjXdZ_kXJNXXjwtEsiQg\nhttps://www.youtube.com/channel/UCyESqWhpBCGuj1f3BrvIx6g\nhttps://www.youtube.com/channel/UCjGxWWACYLoslZlElB0ftSA\nhttps://www.youtube.com/channel/UCe__VNa_DNSNzhSDnMAIpsQ\nhttps://www.youtube.com/channel/UCdB7PV8PPSyyXd7MEh8eDLw\nEste es el canal de twitch que nos apoya (y obviamente el mejor)\nhttps://www.twitch.tv/diablillo_90'

  
def server_in_list(server_id):
  for i in self.server_list:
    if server_id == i:
      return True
      break
  return False
  
def add_server(server_id):
  global server_list
  global spam_head
  global spam_var

  server_list.append({"id":server_id, "head":spam_head, "var":spam_var})
  
def return_head(server_id):
  global server_list
  for i in server_list:
    if i["id"] == server_id:
      return i["head"]
  
def return_var(server_id):
  global server_list
  for i in server_list:
    if i["id"] == server_id:
      return i["var"]
  
def head_complete(server_id):
  global server_list
  state = False
  for i in server_list:
    if i["id"] == server_id:
      return i["head"]
      break
      state = True
  if state == False:
    add_server(server_id)
    return return_head(server_id)
  
def var_complete(server_id):
  global server_list
  state = False
  for i in server_list:
    if i["id"] == server_id:
      return i["var"]
      break
      state = True
  if state == False:
    add_server(server_id)
    return return_var(server_id)

def config_head(server_id, head):
  global server_list

  state = False
  for i in server_list:
    if i["id"] == server_id:
      i["head"] = head
      state = True
      break
  if state == False:
    add_server(server_id)
    for i in server_list:
      if i["id"] == server_id:
        i["head"] = head
        state = True
        break

def config_var(server_id, var):
  global server_list

  state = False
  for i in server_list:
    if i["id"] == server_id:
      i["var"] = var
      state = True
      break
  if state == False:
    add_server(server_id)
    for i in server_list:
      if i["id"] == server_id:
        i["var"] = var
        state = True
        break
