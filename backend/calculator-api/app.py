from flask import Flask, request, jsonify
import math
app=Flask(__name__)
@app.post('/calculate')
def calculate():
    d=request.get_json(force=True)
    status=d.get('factor_status')
    if status!='VERIFIED':
        return jsonify({'status':'BLOCKED','kg_co2e':None,'tco2e':None,'formula':None}),200
    q=d.get('quantity'); f=d.get('factor_value')
    if not isinstance(q,(int,float)) or not isinstance(f,(int,float)) or not math.isfinite(q) or not math.isfinite(f) or q<0 or f<0:
        return jsonify({'status':'BLOCKED','kg_co2e':None,'tco2e':None,'formula':None}),200
    kg=q*f
    return jsonify({'status':'CALCULATED','kg_co2e':kg,'tco2e':kg/1000,'formula':f'{q} × {f}','factor_unit':d.get('factor_unit')}),200
@app.get('/health')
def health(): return jsonify({'status':'ok'})
