# Dynamiskt
# SQL är statiskt
x = "Kimmo"

# Dynamiskt = vi kan ändra på en variabels datatyp under körning
# Användbart men också farligt om man råkar skriva över av misstag
x = 1
x = 1.0
x = True

# Vi kan konkatenera strängar med +. Detta slår ihop strängar
x = "Kimmo" + "12"
# Vi kan inte blanda datatyper hur vi vill y = "Kimmo" + 12 går ej
print(x)

# Booleans (True/False) beter sig ibland som siffror under huven.
# True = 1, False = 0
y = True + True + True
print(y)

# Vi vill printa om en sträng 3 gånger. * fungerar alltså på strängar men inte andra matteoperatorer
print(3*x) # * på sträng ger upprepning

print("The type of variable x is: ", type(x))
print("The type of type is: ", type(type))


# Vi kan använda oss av f-strängar = string interpolation
interpolated_value = 1
f_string = f"This is a string with {interpolated_value}" # ' ' eller " " är båda strängar
# vi kan inuti {} utföra operationer eftersom datatypen inte är omvandlad än


# Vi kan typkonvertera typer.
# I princip allt kan konverteras till en sträng med str()
x = 1 # heltal
x = str(1) # nu är detta en sträng "1"
print(x, type(x))

# Vi kan inte typkonvertera andra datatyper alla gånger
# Vissa datatyper är känsligare än andra

# x = "1.5" # fungerar inte att köra int() på
x = 1.5 # men 1.5 går att omvandla till en int
x = int(x) # detta fungerar, men inte om x = "1.5"


# En funktion skapas med keyword def och allt inuti funktionen ska indenteras
def my_function():
    x = 1


# En funktion introducerar lokalt scope vilket kan ställa till det
x = 2 # x nummer 1


# x inuti funktionen är inte samma som x utanför funktionen
# Använd helst beskrivande namn!
def y(x, y): # x nummer 2
	x = x ** y # x nummer 3
	return x

x = y(2, 3) # nu kör vi funktionen


# indentering skapar inte ett lokalt scope
# if-satsen nedan påverkar det globala scopet.
# funktioner och klasser har lokalt scope (och moduler)
if True:
	x = 100
	
print(x)



# Här är funktionen ovan med med beskrivande variabelnamn
# Betydligt mer lättläst!
base = 2
exponent = 3

def raise_to_power(base, exponent):
	return base ** exponent

result = raise_to_power(base, exponent)


# Funktion som gör att första bokstaven i varje ord blir stor bokstav, resten små.
# Jämför med pythons title()
def bad_name(input_string): # vi skickar in en textsträng, tex "banan apelsin"
	temp = input_string.split(' ')
	
	result = '' # tom sträng
	for t in temp:
		result =  t[0].upper() + t[1::].lower() + ' '

	return result.strip() # strip tar bort whitespace i slutet



# Vi kan importera från Pythons standardbibliotek med keyword import
# Vi kan använda oss av alias för att korta ner namnet om vi vill
import math as m


print(0.1 + 0.2 == 0.3)

# math-biblioteket innehåller färdigskrivna funktioner.
# till exempel isclose() och round()
# dessa kräver att vi skriver alias eller biblioteksnamnet och sedan använder dot notation
result = m.isclose(0.1 + 0.2, 0.3)
print(result)