from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

positions = []
rm = {'deposit': 0, 'risk_pct': 0, 'risk_dollar': 0, 'max_positions': 0, 'risk_per_trade_pct': 0, 'risk_per_trade_dollar': 0}

@app.route('/')
def home():
    return render_template('home.html', positions=positions, rm=rm)

@app.route('/add_position', methods=['POST'])
def add_position():
    position = {
        'pair': request.form['pair'],
        'stop_loss_pct': request.form['stop_loss_pct'],
        'stop_loss_dollar': request.form['stop_loss_dollar'],
        'take_profit_pct': request.form['take_profit_pct'],
        'take_profit_dollar': request.form['take_profit_dollar'],
        'volume': request.form['volume'],
        'risk_reward': request.form['risk_reward']
    }
    positions.append(position)
    return redirect('/')

@app.route('/remove_position', methods=['POST'])
def remove_position():
    index = int(request.form['index'])
    del positions[index]
    return redirect('/')

@app.route('/update_rm', methods=['POST'])
def update_rm():
    rm['deposit'] = request.form['deposit']
    rm['risk_pct'] = request.form['risk_pct']
    rm['risk_dollar'] = request.form['risk_dollar']
    rm['max_positions'] = request.form['max_positions']
    rm['risk_per_trade_pct'] = request.form['risk_per_trade_pct']
    rm['risk_per_trade_dollar'] = request.form['risk_per_trade_dollar']

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
{% extends 'base.html' %}

{% block content %}
  <h2>Мой РМ:</h2>
  <p>Депозит: {{ rm.deposit }}</p>
  <p>Риск на депозит (в процентах): {{ rm.risk_pct }}%</p>
  <p>Риск на депозит (в долларах): {{ rm.risk_dollar }}</p>
  <p>Максимальное число позиций: {{ rm.max_positions }}</p>
  <p>Риск на сделку (в процентах): {{ rm.risk_per_trade_pct }}%</p>
  <p>Риск на сделку (в долларах): {{ rm.risk_per_trade_dollar }}</p>

  <hr>

  <h2>Мои позиции:</h2>
  <table class="table table-striped">
    <thead>
      <tr>
        <th>Position</th>
        <th>Trading pair</th>
        <th>Stop loss in %</th>
        <th>Stop loss in dollars</th>
        <th>Take profit in %</th>
        <th>Take profit in dollars</th>
        <th>Volume</th>
        <th>Risk/reward</th>
      </tr>
    </thead>
    <tbody>
      {% for index, position in enumerate(positions) %}
        <tr>
          <td>{{ index+1 }}</td>    
