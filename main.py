from fastapi import FastAPI, UploadFile, File, HTTPException
from schemas import Application, Dependency
from database import applications, dependencies, app_counter, dep_counter
from osv_client import fetch_vulnerabilities

app=FastAPI()

@app.post("/applicatoions")
async def create_applications(name: str, description: str, file: UploadFile = File(...)):
  global app_counter, dep_counter

  app_id = app_counter
  applications[app_id]=Application(id=app_id, name=name, description=description, dependencies=[])
  app_counter +=1

  #process requirements.txt
  content = await file.read()
  lines = content.decode().splitlines()
  for line in lines:
    if "==" in line:
      dep_name, dep_version = line.split("==")
      vulns = fetch_vulnerabilities(dep_name, dep_version).get("vulns",[])

  dep_id= dep_counter
  dependency =Dependency(id=dep_id, name=dep_name, version=dep_version, vulnerabilities=[v["id"] for v in vulns])
  applications[app_id].dependencies.append(dependency)
        dependencies[dep_id] = dpendency
        dep_counter +=1
   return appliocatoins[app_id]

@app.get("/applicatoions/")
def list_applications():
  return applications.values()

@app.get("/applications/{app_id}/dependencies/")
def get_application_dependencies(app_id: int):
  if app_id not in applications:
    raise HTTPExcception(status_code=404, detail="Application not found")
  return applications[app_id].dependencies

@app.get("/dependencies/")
def list_dependencies():
  return dependencies.values()

@app.get("/dependencies/{dep_id}/")
def get_dependency(dep_id: int):
  if dep not in dependencies:
    raise HTTPException(status_code=404, detail="Dependency not found")
  return dependencies[depid]
