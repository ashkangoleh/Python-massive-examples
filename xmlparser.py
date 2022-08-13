import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("simple.xml")
    
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    
    skills = doc.getElementsByTagName("skill")
    for skill in skills:
        print(skill.getAttribute("name"))
        
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","airflow")
    doc.firstChild.appendChild(newSkill)
    
    skills = doc.getElementsByTagName("skill")
    for skill in skills:
        print(skill.getAttribute("name"))
main()