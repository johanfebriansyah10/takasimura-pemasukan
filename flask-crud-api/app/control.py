from app.models import data


def getAllData():
  return data;

def getDataById(id):
  for item in data:
    if item['id'] == id:
      return item;
    return None;
  
  
def createData(newItem):
  newItem['id'] = len(data) + 1;
  data.append(newItem);
  return newItem;


def UpdateData(id, updatedItem):
  for index, item in enumerate(data):
    if item['id'] == id:
      data[index].update(updatedItem);
      return data[index];
    
  return None;

def delete(id):
  global data;
  data = [item for item in data if item['id'] != id]
  return True;