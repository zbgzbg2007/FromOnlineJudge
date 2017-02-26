//	Problem: Turn Iterator<Iterator<String>> into Iterator<String>, you only need to implement 			two methods: hasNext() and next()


import java.util.*;

public class Iterators{
	private static Iterator<String> flatten(Iterator<Iterator<String> > iters){
		if (iters==null)
			throw new IllegalArgumentException("Iterators can't be null");
		return new Iterator<String>(){
			private LinkedList<Iterator<String> > its;
			//we need this list to store the Iterators we have seen			
			public boolean hasNext(){
				if (its==null)
					its=new LinkedList<Iterator<String> >();
				Iterator<String> it;
				if (its.isEmpty()!=true)
					return true;
				while (iters.hasNext()){
					it=iters.next();
					if (it!=null&&it.hasNext()){
						its.addLast(it);
						return true;
					}
				}
				return false;
			}
			public String next(){
				if (its==null)
					its=new LinkedList<Iterator<String> >();
				Iterator<String> it;
				String s=null;
				if (its.isEmpty()!=true)
				{
					it=its.getFirst();
					its.removeFirst();
					s=it.next();
					if (it.hasNext())
						its.addFirst(it);
					return s;
				}
				while (iters.hasNext()){
					it=iters.next();
					if (it!=null&&it.hasNext())
					{
						s=it.next();
						if (it.hasNext())
							its.addLast(it);
					}
				}
				return s;
			}
		};
	}
	
	public static void main(String[] args){
		List<String> list=new ArrayList<String>();
		list.add("aa");
		list.add("bb");
		list.add("cc");
		List<String> list2=new ArrayList<String>();
		list2.add("dd");
		List<String> list3=new ArrayList<String>();
		List<String> list4=new ArrayList<String>();
		list4.add("ee");
		List<Iterator<String> > iterslist=new ArrayList<Iterator<String> >();
		iterslist.add(list.iterator());
		iterslist.add(list2.iterator());
		iterslist.add(list3.iterator());
		iterslist.add(list4.iterator());
		Iterator<Iterator<String> > iters=iterslist.iterator();
/*		Iterator<String> k=iters.next();
		k=iters.next();
		String t=k.next();System.out.println(t);
		String t=it.next();
		System.out.println(t);
*/		Iterator<String> it=flatten(iters);
		while (it.hasNext()){
			String s=it.next();
			System.out.println(s);
		}
	}


}
