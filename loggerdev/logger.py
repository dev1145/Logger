import logging, sys, psutil, os
import logging.handlers

  
def get_logger(
  logger_name=__name__,
  log_filename=None, log_dir='logs', auto_code_debug=True,
  logging_stream=sys.stderr, log_level=logging.INFO,
  reset=False, propagate=False):
  ''' logger is returned. log_filename or logging_stream is used when auto_code_debug=True, but both are used when auto_code_debug="Both" 
  '''
  #--
  if(reset):
      #[logging.root.removeHandler(handler) for handler in logging.root.handlers[:]]
      [logging.getLogger(logger_name).removeHandler(handler) for handler in logging.getLogger(logger_name).handlers[:]]
  formatter = logging.Formatter(
      fmt='%(asctime)s.%(msecs)03d - %(thread)d - %(name)s -%(filename)s:%(lineno)d - %(levelname)s : %(message)s',
      datefmt='%Y/%m/%d %H:%M:%S',
      style='%')
  # if(len(logging.root.handlers[:])==0):
  #     logging.basicConfig( stream=logging_stream,
  #         format='%(asctime)s %(levelname)s %(message)s', 
  #         level=logging.INFO, 
  #         datefmt='%m/%d/%Y %I:%M:%S %p', filemode = 'w'
  #         )
  logger = logging.getLogger(logger_name)
  if(logger.handlers or logger.hasHandlers()): #hasHandlers check parents logger in dot(.) hierarchy
      return logger
  logger.propagate = propagate

  if(log_filename==None and auto_code_debug==False):
      ch = logging.StreamHandler(stream=logging_stream)
  elif((auto_code_debug==True or auto_code_debug=='Both') and (log_filename != None)):
      me = psutil.Process() #python.exe
      #log_filename='./output/log_'
      #log_file = os.path.realpath(os.path.abspath(os.path.join(me.as_dict()['cwd'], log_filename+"_log.txt" ))) #log_filename+ str(me.pid )
      log_file = os.path.realpath(os.path.abspath(os.path.join(me.as_dict()['cwd'], log_dir, log_filename+"_log.txt" )))
      #-- Temporary Scripts, should be modified...
      if not os.path.exists(log_dir):
          os.makedirs(log_dir)
      #--
      while(me != None):
          if( str(me.name()).startswith('code') or str(me.name()).startswith('Code') ): break
          me = me.parent()
      #print(me)
      #--
      if(me!=None and auto_code_debug!='Both'): #if this was runned by Code, then log output stream is set to stderr
          ch = logging.StreamHandler(stream=logging_stream)
      else: #else log_file + pid
          #ch = logging.FileHandler(filename=log_file, mode='w')
          ch = logging.handlers.RotatingFileHandler(filename=log_file, encoding='utf-8', maxBytes=40*1000*1000, backupCount=15)
          if(auto_code_debug=='Both'):
              ch2 = logging.StreamHandler(stream=logging_stream)
              logger.addHandler(ch2)
              ch2.setLevel(logging.NOTSET)
              ch2.setFormatter(formatter)
  elif (log_filename != None):
      if not os.path.exists(log_dir):
          os.makedirs(log_dir)
      log_file = os.path.realpath(os.path.abspath(os.path.join(me.as_dict()['cwd'], log_dir, log_filename+"_log.txt" if type(log_filename) == str else logger_name+"_log.txt")))
      ch=logging.handlers.RotatingFileHandler(filename=log_file, encoding='utf-8', maxBytes=40*1000*1000, backupCount=15)
  else :
      ch = logging.StreamHandler(stream=logging_stream)

  #formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
  ch.setFormatter(formatter)
  logger.addHandler(ch)
  #ch.setLevel(logging.WARNING)
  ch.setLevel(logging.NOTSET)
  #logging.info('%s',"log_output was set")
  logger.setLevel(log_level)

  return logger
