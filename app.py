from flask import Flask, render_template, request
import scipy.stats as stats

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/continuous')
def continuous():
    return render_template('continuous.html')

@app.route('/discrete')
def discrete():
    return render_template('discrete.html')

# Continuous distributions
@app.route('/continuous/beta', methods=['GET', 'POST'])
def beta():
    if request.method == 'POST':
        x = float(request.form['x'])
        alpha = float(request.form['alpha'])
        beta = float(request.form['beta'])
        result = {
            'P(X < x)': stats.beta.cdf(x, alpha, beta),
            'P(X > x)': 1 - stats.beta.cdf(x, alpha, beta)
        }
        return render_template('results.html', result=result, distribution="Beta Distribution")
    return render_template('beta.html')

@app.route('/continuous/gamma', methods=['GET', 'POST'])
def gamma():
    if request.method == 'POST':
        x = float(request.form['x'])
        shape = float(request.form['shape'])
        scale = float(request.form['scale'])
        result = {
            'P(X < x)': stats.gamma.cdf(x, shape, scale),
            'P(X > x)': 1 - stats.gamma.cdf(x, shape, scale)
        }
        return render_template('results.html', result=result, distribution="Gamma Distribution")
    return render_template('gamma.html')

@app.route('/continuous/exponential', methods=['GET', 'POST'])
def exponential():
    if request.method == 'POST':
        x = float(request.form['x'])
        lambda_1 = float(request.form['lambda'])
        result = {
            'P(X < x)': stats.expon.cdf(x, scale=1/lambda_1),
            'P(X > x)': 1 - stats.expon.cdf(x, scale=1/lambda_1)
        }
        return render_template('results.html', result=result, distribution="Exponential Distribution")
    return render_template('exponential.html')

@app.route('/continuous/normal', methods=['GET', 'POST'])
def normal():
    if request.method == 'POST':
        x = float(request.form['x'])
        mean = float(request.form['mean'])
        std_dev = float(request.form['std_dev'])
        result = {
            'P(X < x)': stats.norm.cdf(x, mean, std_dev),
            'P(X > x)': 1 - stats.norm.cdf(x, mean, std_dev)
        }
        return render_template('results.html', result=result, distribution="Normal Distribution")
    return render_template('normal.html')

# Discrete distributions
@app.route('/discrete/binomial', methods=['GET', 'POST'])
def binomial():
    if request.method == 'POST':
        x = int(request.form['x'])
        n = int(request.form['n'])
        p = float(request.form['p'])
        result = {
            'P(X = x)': stats.binom.pmf(x, n, p),
            'P(X > x)': 1 - stats.binom.cdf(x, n, p),
            'P(X < x)': stats.binom.cdf(x, n, p)
        }
        return render_template('results.html', result=result, distribution="Binomial Distribution")
    return render_template('binomial.html')

@app.route('/discrete/geometric', methods=['GET', 'POST'])
def geometric():
    if request.method == 'POST':
        x = int(request.form['x'])
        p = float(request.form['p'])
        result = {
            'P(X = x)': stats.geom.pmf(x, p),
            'P(X > x)': 1 - stats.geom.cdf(x, p),
            'P(X < x)': stats.geom.cdf(x, p)
        }
        return render_template('results.html', result=result, distribution="Geometric Distribution")
    return render_template('geometric.html')

@app.route('/discrete/hypergeometric', methods=['GET', 'POST'])
def hypergeometric():
    if request.method == 'POST':
        x = int(request.form['x'])
        cap_n = int(request.form['cap_n'])
        r = int(request.form['r'])
        n = int(request.form['n'])
        result = {
            'P(X = x)': stats.hypergeom.pmf(x, cap_n, r, n),
            'P(X > x)': 1 - stats.hypergeom.cdf(x, cap_n, r, n),
            'P(X < x)': stats.hypergeom.cdf(x, cap_n, r, n)
        }
        return render_template('results.html', result=result, distribution="Hypergeometric Distribution")
    return render_template('hypergeometric.html')

@app.route('/discrete/poisson', methods=['GET', 'POST'])
def poisson():
    if request.method == 'POST':
        x = int(request.form['x'])
        lambda_2 = float(request.form['lambda'])
        result = {
            'P(X = x)': stats.poisson.pmf(x, lambda_2),
            'P(X > x)': 1 - stats.poisson.cdf(x, lambda_2),
            'P(X < x)': stats.poisson.cdf(x, lambda_2)
        }
        return render_template('results.html', result=result, distribution="Poisson Distribution")
    return render_template('poisson.html')

if __name__ == "__main__":
    app.run(debug=True)
