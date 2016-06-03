import json
import psycopg2

connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

def parse_file():
    projectname = "columba-1.4-src"
    with open("../smell-detector-results/columba_smells.json") as json_file:
        json_data = json.load(json_file)
        
        number_of_analyzed_classes = len(json_data)
        for json_object in json_data:

            smelly_files = set()
            found_smells = set()
            has_bad_smell =  False

            for method in json_object['methods']:
                for smells_node_children in method['smells']:
                    has_bad_smell = True
                    smelly_files.add(json_object['fullyQualifiedName'])
                    found_smells.add(smells_node_children['name'])
              
            for smells_node_children in json_object['smells']:
                has_bad_smell = True
                found_smells.add(smells_node_children['name'])
                smelly_files.add(json_object['fullyQualifiedName'])

            if has_bad_smell:
                cursor.execute("insert into tse_smell_detector_results (projectname, classname, code_smell_list) values (%s,%s,%s)", (projectname, ','.join(smelly_files), ','.join(found_smells)))
                connection.commit()

def display_results():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:
        total_number_of_files = 0
        total_number_of_fiels_with_bad_smell = 0
        total_number_of_files_with_self_admitted_td = 0
        total_intersection_number = 0
        
        projectname = project[0]

        cursor.execute("select count(*) from comment_class where projectname = %s", (projectname,))
        total_number_of_files = cursor.fetchone()[0]

        # cursor.execute("select count(*) from tse_smell_detector_results a, comment_class b where a.classname = b.classname and a.projectname = '"+projectname+"' and a.code_smell_list similar to '%(FeatureEnvy|LazyClass|LongParameterList|LongMethod|ComplexClass|MessageChain|SpeculativeGenerality|SpaghettiCode|ClassDataShouldBePrivate|BlobClass|RefusedBequest)%'")
        cursor.execute("select count(*) from tse_smell_detector_results a, comment_class b where a.classname = b.classname and a.projectname = '"+projectname+"' and a.code_smell_list similar to '%(LongParameterList|LongMethod|ComplexClass|MessageChain|SpeculativeGenerality|SpaghettiCode|ClassDataShouldBePrivate|BlobClass|RefusedBequest)%'")
        total_number_of_fiels_with_bad_smell = cursor.fetchone()[0]

        cursor.execute("select distinct(a.classname) from comment_class a, processed_comment b  where a.id = b.commentclassid  and a.projectname = %s and b.classification in ('DESIGN', 'REQUIREMENT')", (projectname,))
        files_with_self_admitted_td = cursor.fetchall()
        total_number_of_files_with_self_admitted_td = len(files_with_self_admitted_td)

        for file_name in files_with_self_admitted_td:
            classname = file_name[0]
            # cursor.execute("select count(*) from tse_smell_detector_results a, comment_class b where a.classname = b.classname and a.projectname = '"+projectname+"' and a.classname = '"+classname+"' and a.code_smell_list similar to '%(FeatureEnvy|LazyClass|LongParameterList|LongMethod|ComplexClass|MessageChain|SpeculativeGenerality|SpaghettiCode|ClassDataShouldBePrivate|BlobClass|RefusedBequest)%'") 
            cursor.execute("select count(*) from tse_smell_detector_results a, comment_class b where a.classname = b.classname and a.projectname = '"+projectname+"' and a.classname = '"+classname+"' and a.code_smell_list similar to '%(LongParameterList|LongMethod|ComplexClass|MessageChain|SpeculativeGenerality|SpaghettiCode|ClassDataShouldBePrivate|BlobClass|RefusedBequest)%'") 
            result = cursor.fetchone()[0]
            if result != 0 :
                total_intersection_number = total_intersection_number + 1

        # print ("projectname", projectname)
        # print ("total_number_of_files", total_number_of_files)
        # print ("total_number_of_fiels_with_bad_smell", total_number_of_fiels_with_bad_smell)
        # print ("total_number_of_files_with_self_admitted_td", total_number_of_files_with_self_admitted_td)
        # print ("total_intersection_number", total_intersection_number)

        print (projectname, "&", total_number_of_files, "&", total_number_of_fiels_with_bad_smell, "&", total_number_of_files_with_self_admitted_td, "&", total_intersection_number )

def tokenize_smells():

    cursor.execute("select a.code_smell_list from tse_smell_detector_results a, comment_class b where a.classname = b.classname ")
    results =  cursor.fetchall()

    smell_dictionary = {}

    for line  in results:
        tokens = line[0].split(',')
        for token in tokens:
            if token in smell_dictionary:
                smell_dictionary[token] = smell_dictionary[token] + 1
            else:
                smell_dictionary[token] =  1

    print (smell_dictionary)
         
def tokenize_smells_by_project():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:    
        projectname = project[0]         
        
        cursor.execute("select code_smell_list from tse_smell_detector_results a, comment_class b where a.classname = b.classname and b.projectname=%s", (projectname, ))
        results =  cursor.fetchall()

        smell_dictionary = {}
    
        for line  in results:
            tokens = line[0].split(',')
            for token in tokens:
                if token in smell_dictionary:
                    smell_dictionary[token] = smell_dictionary[token] + 1
                else:
                    smell_dictionary[token] =  1

        print (projectname, smell_dictionary)
        
display_results()
# tokenize_smells_by_project()

