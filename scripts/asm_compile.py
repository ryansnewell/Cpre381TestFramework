import subprocess

def sim_asm(asm_file=None):

    if asm_file:
        path = asm_file
    else:
        print('Please provide an assembly file to run.')
        path = input('>').strip()
        print('Sim-ing input file: ' + path)
    
    mars_dump_file = open('temp/mars_dump.out', 'w+')
    subprocess.call(
            ['java','-jar','dependencies/Mars_CPRE381_SIMD_v1.jar','nc',path],
            stdout=mars_dump_file
    )
    mars_dump_file.close()

if __name__ == '__main__':
        try:
            sim_asm()
        except KeyboardInterrupt:
            exit(1)
        except Exception as e:
            print('Exited with unexpected excetpion:\n')
            print(e)
