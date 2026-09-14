from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import os

app=FastAPI(title='SCS AIC Portal API',version='3.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=False,allow_methods=['GET'],allow_headers=['*'])
@app.get('/')
def root(): return {'service':'SCS AIC School Portal','status':'online','time':datetime.now(timezone.utc).isoformat()}
@app.get('/health')
def health(): return {'status':'healthy','version':'3.0.0'}
@app.get('/api/config')
def config(): return {'supabase_url':os.getenv('SUPABASE_URL','https://yvadmztokmlijsknyuhu.supabase.co'),'mode':'supabase-client'}
