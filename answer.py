import pandas as pd

paper_author = pd.read_csv('Desktop/paper_author.csv')
paper_reference = pd.read_csv('Desktop/paper_reference.csv')


def answer1():
    df = pd.DataFrame({'author_id':[''], 'publication_count' : [''], 'citation_count' : ['']})
    for i in range(len(paper_author)):
        author_id = paper_author['author_id'][i]
        if author_id in list(df['author_id']):
            citation_count = df.loc[df['author_id'] == author_id][df.columns[2]]
            paper_id = paper_author['paper_id'][i]
            if paper_id in list(paper_reference['reference_paper_id']) :
                citation_count += paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count += 0 
            df.loc[df['author_id'] == author_id, 'citation_count'] = citation_count

        else:
            publication_count = paper_author.groupby('author_id').size()[author_id]
            paper_id = paper_author['paper_id'][i]
            citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            df=df.append({'author_id' : author_id, 'publication_count' : publication_count, 'citation_count' : citation_count} , ignore_index=True)
    df = df.sort_index()
    df = df.drop(0 ,axis=0)
    return df
            
def answer2():
    df = pd.DataFrame({'author_id':[''], 'year':[''], 'publication_count' : [''], 'citation_count' : ['']})

    for i in range(len(paper_author)):
        author_id = paper_author['author_id'][i]
        if author_id in list(df['author_id']):
            pass
        else:
            year = 0
            for j in paper_author[paper_author['author_id'] == author_id].index:
                published_year = paper_author['published_at'][j].split('-')[0]
                if year == published_year:
                    index = df[(df['author_id'] == author_id) & (df['year'] == year)].index
                    df.publication_count[index] += 1
                    paper_id = paper_author['paper_id'][j]
                    if paper_id in list(paper_reference['reference_paper_id']):
                        df.citation_count[index] += paper_reference.groupby('reference_paper_id').size()[paper_id] 
                    else:
                        citation_count += 0
                else:
                    publication_count = 1
                    paper_id = paper_author['paper_id'][j]
                    year = paper_author['published_at'][j].split('-')[0]
                    if paper_id in list(paper_reference['reference_paper_id']):
                        citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
                    else:
                        citation_count = 0
                    df = df.append({'author_id' : author_id, 'year' : int(year) , 'publication_count' : publication_count, 'citation_count' : citation_count} , ignore_index=True)
    df = df.sort_index()
    df = df.drop(0 ,axis=0)
    return df

        
def answer3():
    df = pd.DataFrame({'author_id':[''], 'yearmonth':[''], 'publication_count' : [''], 'citation_count' : ['']})

    for i in range(len(paper_author)):
        author_id = paper_author['author_id'][i]
        if author_id in list(df['author_id']):
            pass
        else:
            yearmonth = 0
            for j in paper_author[paper_author['author_id'] == author_id].index:
                published_yearmonth = paper_author['published_at'][j][0:7]
                if yearmonth == published_yearmonth:
                    index = df[(df['author_id'] == author_id) & (df['yearmonth'] == yearmonth)].index
                    df.publication_count[index] += 1
                    paper_id = paper_author['paper_id'][j]
                    if paper_id in list(paper_reference['reference_paper_id']):
                        df.citation_count[index] += paper_reference.groupby('reference_paper_id').size()[paper_id] 
                    else:
                        citation_count += 0
                else:
                    publication_count = 1
                    paper_id = paper_author['paper_id'][j]
                    yearmonth = paper_author['published_at'][j][0:7]
                    if paper_id in list(paper_reference['reference_paper_id']):
                        citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
                    else:
                        citation_count = 0
                    df = df.append({'author_id' : author_id, 'yearmonth' : yearmonth , 'publication_count' : publication_count, 'citation_count' : citation_count} , ignore_index=True)

    df = df.sort_index()
    df = df.drop(0 ,axis=0)
    return df
                    
def answer4():
    df = pd.DataFrame({'author_id':[''], 'hindex':['']})
    author_citation_count=0

    author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
    for i in author_id_list:
        author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
        for j in paper_author[paper_author['author_id'] == i].index:
            year = int(paper_author.published_at[j].split('-')[0])
            paper_id = paper_author['paper_id'][j]
            if paper_id in list(paper_reference['reference_paper_id']):
                citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count = 0
            author = author.append({'year': year,'paper_id': paper_id, 'citation_count':citation_count}, ignore_index=True)
        author = author.drop(0 ,axis=0)
        author_citation_count= sorted(author.citation_count,reverse=True)
        for j in range(len(author_citation_count)):
            if author_citation_count[j] == j+1:
                hindex = j+1
                df = df.append({'author_id': i , 'hindex': hindex}, ignore_index=True)
                break  
            elif author_citation_count[j] < j+1:
                hindex = j+2
                df = df.append({'author_id': i , 'hindex': hindex}, ignore_index=True)
                break    
    df = df.drop(0 ,axis=0)
    return df

def answer5():
    df = pd.DataFrame({'author_id':[''], 'h5index':['']})
    author_id_list = list(set(paper_author.author_id))
    for i in author_id_list:
        author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
        for j in paper_author[paper_author['author_id'] == i].index:
            year = int(paper_author.published_at[j].split('-')[0])
            paper_id = paper_author['paper_id'][j]
            if paper_id in list(paper_reference['reference_paper_id']):
                citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count = 0
            author = author.append({'year': year,'paper_id': paper_id, 'citation_count':citation_count}, ignore_index=True)
        author = author.drop(0 ,axis=0)
        for j in range(len(author),0,-1):
            if author.year[j] <= 2021 and author.year[j] >= 2017: 
                pass
            else:
                author = author.drop(j ,axis=0)
        author_citation_count= sorted(author.citation_count,reverse=True)
        for j in range(len(author_citation_count)):
            if author_citation_count[j] == j+1:
                hindex = j+1
                df = df.append({'author_id': i , 'h5index': hindex}, ignore_index=True)
                break  
            elif author_citation_count[j] < j+1:
                hindex = j+2
                df = df.append({'author_id': i , 'h5index': hindex}, ignore_index=True)
                break   
    df = df.drop(0 ,axis=0)
    return df

def answer6():
    df = pd.DataFrame({'author_id':[''], 'year' : [''] ,'hindex':['']})
    author_id_list = list(set(paper_author.author_id))
    for i in author_id_list:
        author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
        for j in paper_author[paper_author['author_id'] == i].index:
            year = int(paper_author.published_at[j].split('-')[0])
            paper_id = paper_author['paper_id'][j]
            if paper_id in list(paper_reference['reference_paper_id']):
                citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count = 0
            author = author.append({'year': year,'paper_id': paper_id, 'citation_count':citation_count}, ignore_index=True)
        author = author.drop(0 ,axis=0)

        author_year_list = sorted(list(set(author.year)))

        for j in author_year_list:
            author_copy = author
            for k in range(len(author),0,-1):
                if author_copy.year[k] <= j:
                    pass
                else:
                    author_copy = author_copy.drop(k ,axis=0)
            author_citation_count= sorted(author_copy.citation_count,reverse=True)

            for k in range(len(author_citation_count)):
                if len(author_citation_count) == k+1:
                    hindex = k+1
                    df = df.append({'author_id': i , 'year' : j , 'hindex' : hindex}, ignore_index=True)
                    break
                elif author_citation_count[k] > k+1:
                    pass 
                else: 
                    hindex = k+1
                    df = df.append({'author_id': i , 'year' : j , 'hindex' : hindex}, ignore_index=True)
                    break
    df = df.drop(0 ,axis=0)
    return df

def answer7():
    df = pd.DataFrame({'author_id':[''], 'year' : [''] ,'h5index':['']})
    author_id_list = list(set(paper_author.author_id))
    for i in author_id_list:
        author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
        for j in paper_author[paper_author['author_id'] == i].index:
            year = int(paper_author.published_at[j].split('-')[0])
            paper_id = paper_author['paper_id'][j]
            if paper_id in list(paper_reference['reference_paper_id']):
                citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count = 0
            author = author.append({'year': year,'paper_id': paper_id, 'citation_count':citation_count}, ignore_index=True)
        author = author.drop(0 ,axis=0)

        author_year_list = sorted(list(set(author.year)))

        for j in author_year_list:
            author_copy = author
            for k in range(len(author),0,-1):
                if author_copy.year[k] <= j and author_copy.year[k] >= j-4:
                    pass
                else:
                    author_copy = author_copy.drop(k ,axis=0)
            author_citation_count= sorted(author_copy.citation_count,reverse=True)

            for k in range(len(author_citation_count)):
                if len(author_citation_count) == k+1:
                    h5index = k+1
                    df = df.append({'author_id': i , 'year' : j , 'h5index' : h5index}, ignore_index=True)
                    break
                elif author_citation_count[k] > k+1:
                    pass 
                else: 
                    h5index = k+1
                    df = df.append({'author_id': i , 'year' : j , 'h5index' : h5index}, ignore_index=True)
                    break
    df = df.drop(0 ,axis=0)
    return df

def answer8():
    df = pd.DataFrame({'author_id':[''], 'yearmonth' : [''] ,'h5index':['']})      
    author_id_list = list(set(paper_author.author_id))
    for i in author_id_list:
        author = pd.DataFrame({'year': [''],'paper_id': [''], 'citation_count':['']})
        for j in paper_author[paper_author['author_id'] == i].index:
            year= paper_author.published_at[j].split('-')[0]
            month= paper_author.published_at[j].split('-')[1]
            paper_id = paper_author['paper_id'][j]
            if paper_id in list(paper_reference['reference_paper_id']):
                citation_count = paper_reference.groupby('reference_paper_id').size()[paper_id] 
            else:
                citation_count = 0
            author = author.append({'year': year, 'month': month,'paper_id': paper_id, 'citation_count':citation_count}, ignore_index=True)

        author = author.drop(0 ,axis=0)

        author_copy = author
        for k in range(1,len(author.year)+1):
            before = str(int(author.year[k])-4) + '-' + author.month[k]
            yearmonth = author.year[k] + '-' + author.month[k]
            days  = pd.to_datetime(yearmonth) - pd.to_datetime(before)
            author_copy = author
            for l in range(len(author.year),k-1,-1):
                yearmonth = author_copy.year[l] + '-' + author_copy.month[l]
                if pd.to_datetime(yearmonth) - pd.to_datetime(before) <= days:
                    pass
                else:
                    author_copy = author_copy.drop(l,axis=0)

            author_citation_count= sorted(author_copy.citation_count,reverse=True)

            for l in range(len(author_citation_count)):
                if len(author_citation_count) == l+1:
                    h5index = l+1
                    df = df.append({'author_id': i , 'yearmonth' : yearmonth , 'h5index' : h5index}, ignore_index=True)
                    break
                elif author_citation_count[l] > l+1:
                    pass 
                else: 
                    h5index = l+1
                    df = df.append({'author_id': i , 'yearmonth' : yearmonth , 'h5index' : h5index}, ignore_index=True)
                    break
    df = df.drop(0 ,axis=0)
    return df
