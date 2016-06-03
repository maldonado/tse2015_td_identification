import psycopg2

connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

def parse_god_classes_files():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:
        projectname = project[0] 
        try:
            with open("../IEEEtran/Revision1/jdeodorant_code_smells/"+projectname+"_god_class.txt") as result_file:
        
                file_data = result_file.read().split('\n')
                god_classes = set()
            
                for file_line in file_data:
                    tokens = file_line.split('\t')
                    if tokens[0] is not '':
                        god_classes.add(tokens[0])
                
                for god_class in god_classes:
                    cursor.execute("insert into tse_jdeodorant_results (projectname, classname, code_smell_list) values (%s, %s, 'god_class')", (projectname, god_class))
                    connection.commit()
          
                print (len(god_classes))

        except Exception:
            pass
    
        
def parse_feature_envy_classes_files():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:
        projectname = project[0]

        try:
            with open("../IEEEtran/Revision1/jdeodorant_code_smells/"+projectname+"_feature_envy.txt") as result_file:
            
                file_data = result_file.read().split('\n')      
                feature_envy_classes = set()

                for file_line in file_data:
                    tokens = file_line.split('\t')
                    if tokens[0] is not '':
                        feature_envy_classes.add(tokens[1].split('::')[0])

                for feature_envy_class in feature_envy_classes:
                    cursor.execute("insert into tse_jdeodorant_results (projectname, classname, code_smell_list) values (%s, %s, 'feature_envy')", (projectname, feature_envy_class))
                    connection.commit()
                        
                print (len(feature_envy_classes))
            
        except Exception:
            pass

def parse_long_method_files():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:
        projectname = project[0]

        try:
            with open("../IEEEtran/Revision1/jdeodorant_code_smells/"+projectname+"_long_method.txt") as result_file:
            
                file_data = result_file.read().split('\n')      
                long_method_classes = set()

                for file_line in file_data:
                    tokens = file_line.split('\t')
                    if tokens[0] is not '':
                        long_method_classes.add(tokens[0])

                for long_method_class in long_method_classes:
                    cursor.execute("insert into tse_jdeodorant_results (projectname, classname, code_smell_list) values (%s, %s, 'long_method')", (projectname, long_method_class))
                    connection.commit()
                    pass
                        
                print (len(long_method_classes))
            
        except Exception:
            pass
    
def display_results():
    cursor.execute("select distinct(projectname) from comment_class")
    projects = cursor.fetchall()

    for project in projects:
        
        total_number_of_files = 0
        total_number_of_files_with_god_class = 0
        total_number_of_files_with_feature_envy = 0
        total_number_of_files_with_long_method = 0
        total_number_of_files_with_bad_smell = 0
        total_number_of_files_with_self_admitted_td = 0
        total_intersection_number_with_god_class = 0
        total_intersection_number_with_feature_envy = 0
        total_intersection_number_with_long_method = 0
        total_intersection_number_with_bad_smells = 0
        
        projectname = project[0]

        
        cursor.execute("select count(*) from comment_class where projectname = %s", (projectname,))
        total_number_of_files = cursor.fetchone()[0]
        
        # god class counter
        cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.code_smell_list = 'god_class'", (projectname, ))
        total_number_of_files_with_god_class = cursor.fetchone()[0]

        # feature envy counter
        cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.code_smell_list = 'feature_envy'", (projectname, ))
        total_number_of_files_with_feature_envy = cursor.fetchone()[0]

        # long method counter
        cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.code_smell_list = 'long_method'", (projectname, ))
        total_number_of_files_with_long_method = cursor.fetchone()[0]

        # all bad smells 
        cursor.execute("select count(distinct(a.classname)) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s", (projectname, ))
        total_number_of_files_with_bad_smell = cursor.fetchone()[0]        

        cursor.execute("select distinct(a.classname) from comment_class a, processed_comment b  where a.id = b.commentclassid  and a.projectname = %s and b.classification in ('DESIGN', 'IMPLEMENTATION')", (projectname,))
        files_with_self_admitted_td = cursor.fetchall()
        total_number_of_files_with_self_admitted_td = len(files_with_self_admitted_td)

        for file_name in files_with_self_admitted_td:
            classname = file_name[0]            
            cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.classname = %s and a.code_smell_list = 'god_class'", (projectname, classname))
            result = cursor.fetchone()[0]
            if result != 0 :
                # print(classname)
                total_intersection_number_with_god_class = total_intersection_number_with_god_class + 1
            # else:
            #     print(classname)

            cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.classname = %s and a.code_smell_list = 'feature_envy'", (projectname, classname))
            result = cursor.fetchone()[0]
            if result != 0 :
                # print(classname)
                total_intersection_number_with_feature_envy = total_intersection_number_with_feature_envy + 1
            # else:
            #     print(classname)

            cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.classname = %s and a.code_smell_list = 'long_method'", (projectname, classname))
            result = cursor.fetchone()[0]
            if result != 0 :
                # print(classname)
                total_intersection_number_with_long_method = total_intersection_number_with_long_method + 1
            # else:
            #     print(classname)

            cursor.execute("select count(*) from tse_jdeodorant_results a, comment_class b where a.classname = b.classname and a.projectname = %s and a.classname = %s", (projectname, classname))
            result = cursor.fetchone()[0]
            if result != 0 :
                # print()
                total_intersection_number_with_bad_smells = total_intersection_number_with_bad_smells + 1

        # print ("total_number_of_files", total_number_of_files)
        # print ("total_number_of_files_with_god_class", total_number_of_files_with_god_class)
        # print ("total_number_of_files_with_feature_envy", total_number_of_files_with_feature_envy)
        # print ("total_number_of_files_with_long_method", total_number_of_files_with_long_method)
        # print ("total_number_of_files_with_bad_smell", total_number_of_files_with_bad_smell)
        # print ("total_number_of_files_with_self_admitted_td", total_number_of_files_with_self_admitted_td)
        # print ("total_intersection_number_with_god_class", total_intersection_number_with_god_class)
        # print ("total_intersection_number_with_feature_envy", total_intersection_number_with_feature_envy)
        # print ("total_intersection_number_with_long_method", total_intersection_number_with_long_method)
        # print ("total_intersection_number_with_bad_smells", total_intersection_number_with_bad_smells)

        print (projectname, "&", total_number_of_files, "&", total_number_of_files_with_bad_smell, "&", total_number_of_files_with_long_method, "&", total_number_of_files_with_feature_envy, "&", total_number_of_files_with_god_class, "&", total_number_of_files_with_self_admitted_td, "&", total_intersection_number_with_bad_smells, "&", total_intersection_number_with_long_method, "&", total_intersection_number_with_feature_envy, "&", total_intersection_number_with_god_class)

# parse_god_classes_files()
# parse_feature_envy_classes_files()
# parse_long_method_files()
display_results()