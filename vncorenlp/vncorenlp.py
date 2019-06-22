from py4j.java_gateway import JavaGateway

class VnCoreNLP:
    def __init__(self, path):
        self.path = path


    def word_tokenizer(self, sentence):
        gateway = JavaGateway.launch_gateway(classpath=self.path, die_on_exit=True)
        annotators = gateway.new_array(gateway.jvm.java.lang.String, 1)

        annotators[0] = 'wseg'
        
        pipeline = gateway.jvm.vn.pipeline.VnCoreNLP(annotators)
        
        annotation = gateway.jvm.vn.pipeline.Annotation(sentence)
        pipeline.annotate(annotation)
        tokens = annotation.toString().split()
        result = []
        pos = 1
        
        while pos < len(tokens):
            result.append(tokens[pos])
            pos += 6

        return result
