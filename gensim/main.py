import sys
sys.path.append('./lib/')

from gensim import models
from gensim.models.doc2vec import Doc2Vec

def handle(event, context):
# if __name__ == '__main__':
    text = "高齢者が安心して暮らせる 高齢者が安心して暮らせる事が大事だと思います"
    model = Doc2Vec.load('./model/doc2vec.model')

    new_vector = model.infer_vector(text)
    results = model.docvecs.most_similar([new_vector])

    return {
        'results': results
    }
    # print(results)