from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = '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'

def generate_blog_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a detailed blog post about {topic}"}
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    blog_post = generate_blog_post(topic)
    return render_template('index.html', topic=topic, blog_post=blog_post)

if __name__ == '__main__':
    app.run(debug=True)
