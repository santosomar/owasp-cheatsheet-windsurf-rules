---
trigger: glob
globs: [java, cs, cpp, h, c, php, py, swift, m, xml, xsd, xslt, cfml]
---

### 1. Disable DTDs and External Entities
**Do this by default** unless you absolutely need DTD processing. This is your first line of defense.

### 2. Language-Specific Implementation

#### Java
    ```java
    // For DocumentBuilderFactory
    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
    dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
    dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
    dbf.setXIncludeAware(false);
    dbf.setExpandEntityReferences(false);
    
    // For SAXParserFactory
    SAXParserFactory spf = SAXParserFactory.newInstance();
    spf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
    // Set other features as above
    
    // For XMLInputFactory (StAX)
    XMLInputFactory xif = XMLInputFactory.newInstance();
    xif.setProperty(XMLInputFactory.SUPPORT_DTD, false);
    xif.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
    ```
    
    #### .NET
    ```csharp
    // For XmlReader
    XmlReaderSettings settings = new XmlReaderSettings();
    settings.DtdProcessing = DtdProcessing.Prohibit;
    settings.XmlResolver = null;
    XmlReader reader = XmlReader.Create(stream, settings);
    
    // Ensure you're using .NET Framework 4.5.2 or later for full protection
    ```
    
    #### C/C++
    ```c
    // Using libxml2 (version 2.9 or later recommended)
    xmlParserCtxtPtr ctxt = xmlNewParserCtxt();
    // Disable dangerous options
    int options = XML_PARSE_NOENT | XML_PARSE_DTDLOAD;
    xmlDocPtr doc = xmlCtxtReadMemory(ctxt, buffer, size, NULL, NULL, options);
    ```
    
    #### PHP
    ```php
    // For PHP versions before 8.0
    libxml_disable_entity_loader(true); // Deprecated in PHP 8.0+
    
    // Alternative approach
    libxml_set_external_entity_loader(function() {
        return null;
    });
    
    // For SimpleXML
    $options = LIBXML_NONET | LIBXML_DTDATTR;
    $xml = simplexml_load_string($xmlString, 'SimpleXMLElement', $options);
    ```
    
    #### Python
    ```python
    # Best approach: Use defusedxml library
    from defusedxml import ElementTree as ET
    tree = ET.parse('filename.xml')
    
    # Or for lxml with safety features
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    tree = etree.parse('filename.xml', parser)
    ```
    
    #### iOS/macOS
    ```swift
    // Use NSXMLDocument with appropriate options
    let options: NSXMLNodeOptions = .documentTidyXML
    let xmlDoc = try NSXMLDocument(data: data, options: options.union(.nodeLoadExternalEntitiesNever))
    ```
    
    #### ColdFusion
    ```
    // In Application.cfc
    this.xmlFeatures = 'ALLOWEXTERNALENTITIES=false';
    
    // Or directly in cfxml
    <cfxml variable="doc" caseSensitive="true" allowExternalEntities="false">
    ```
    
    ### 3. Additional Security Measures
    
    1. **Update your XML libraries regularly** - Older versions often have XXE vulnerabilities
    
    2. **Sanitize and validate all XML input** - Reject suspicious content before it reaches your parser
    
    3. **Avoid dangerous APIs** - Never use `java.beans.XMLDecoder` on untrusted content
    
    4. **Use static analysis tools** - Implement Semgrep or similar tools to catch risky XML parsing code
    
    5. **Test your defenses** - Try XXE payloads against your application in a safe environment
    
    ### 4. When You Can't Disable DTDs
    
    If you absolutely must process DTDs:
    - Configure an entity resolver that restricts what entities can be loaded
    - Implement strict whitelisting of allowed entities
    - Consider preprocessing XML to remove DOCTYPE declarations
    

    - "Disable DTDs completely in your XML parser configuration whenever possible."
    - "Explicitly disable external entity resolution on your XML parser."
    - "For Java, set `factory.setFeature('http://apache.org/xml/features/disallow-doctype-decl', true)`."
    - "For .NET, set `XmlResolver = null` and `DtdProcessing = Prohibit`."
    - "Use secure parsing libraries like defusedxml (Python) or updated parser versions."
    - "Regularly update XML libraries and frameworks."
    - "Avoid using `java.beans.XMLDecoder` unless inputs are fully trusted."
    - "Test your codebase with static analysis tools specialized in XXE detection."
