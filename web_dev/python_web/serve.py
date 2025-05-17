from livereload import Server

class Selecter:
    def __init__(self):
        self.project_Dict={
                "onehtml_1":"/data/data/com.termux/files/home/project/military-study-log/web_dev/python_web/first_onehtml",
                "template_1":"/data/data/com.termux/files/home/project/military-study-log/web_dev/python_web/first_template"
                }
        self.server=Server()

    def start_serve(self, project):
        self.server.watch('*.html')
        self.server.watch('*.js')
        self.server.watch('*.css')
        self.server.serve(root=self.project_Dict[project]) 
        
    def server_select(self):
        print("project_list")
        project_list=list(self.project_Dict.keys())
        for idx, project in enumerate(project_list):
            print(f"{idx}: {project}")

        project_num=int(input())
        return project_list[project_num]
 

if __name__=="__main__":
    selecter=Selecter()
    project=selecter.server_select()
    selecter.start_serve(project)

   
