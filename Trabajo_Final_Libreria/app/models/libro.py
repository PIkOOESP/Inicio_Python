class libro:
    cantidad_libros = 0
    
    def __init__(self, titulo, isbn, autor, editorial):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__autor = autor
        self.__editorial = editorial
        libro.cantidad_libros += 1
        
    def getTitulo(self):
        return self.__titulo
    
    def getIsbn(self):
        return self.__isbn
    
    def getAutor(self):
        return self.__autor
    
    def getEditorial(self):
        return self.__editorial
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setIsbn(self, isbn):
        self.__isbn = isbn
        
    def setAutor(self, autor):
        self.__autor = autor
        
    def setEditorial(self, editorial):
        self.__editorial = editorial
        
    def mostrar_info(self):
        return f"Titulo:{self.__titulo}\nISBN:{self.__isbn}\nAutor:{self.__autor}\nEditorial:{self.__editorial}"
    
    @classmethod
    def mostrar_total(cls):
        return f"Cantidad total de libros: {cls.cantidad_libros}"