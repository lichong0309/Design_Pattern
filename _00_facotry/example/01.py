class Shape(object):
    def draw(self):
        pass
    
class RectangleImplementsShape(Shape):
    def __init__(self):
        print("this relalize Interface")
        
    def draw(self):
        print("Inside Rectangle::draw() method.")
        
class SquareImplementsShape(Shape):
    def __init__(self):
        print("this relalize Interface")
        
    def draw(self):
        print("Inside Square::draw() method.")
        
        
class CircleImplementsShape(Shape):
    def __init__(self):
        print("this relalize Interface")
        
    def draw(self):
        print("Inside Circle::draw() method.")
        
class ShapeFactory(object):
    def __init__(self):
        print("ShapeFactory init")
        
    def getShape(self,method):
        if method.lower() == 'rectangle':
            return RectangleImplementsShape()
        if method.lower() == 'square':
            return SquareImplementsShape()
        if method.lower() == 'circle':
            return CircleImplementsShape()

            
        
shapeFactory = ShapeFactory()        
        
shap1 = shapeFactory.getShape('Rectangle')
shap2 = shapeFactory.getShape('Square')
shap3 = shapeFactory.getShape('Circle')

shap1.draw()
shap2.draw()
shap3.draw()
